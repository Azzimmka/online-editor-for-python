import os
import re
import subprocess
import sys
import tempfile


def _normalize_tests(test_code: str) -> str:
    lines = []
    for raw_line in test_code.splitlines():
        line = raw_line.rstrip()
        match = re.match(r"(\s*)assert\s+(.+?)\s+==\s+(.+)$", line)
        if match:
            indent, left, right = match.groups()
            lines.append(f"{indent}expect({left}, {right})")
            continue

        match = re.match(r"(\s*)assert\s+(.+?)\s+is\s+(True|False|None)\s*$", line)
        if match:
            indent, expr, literal = match.groups()
            lines.append(f"{indent}expect({expr}, {literal})")
            continue

        lines.append(raw_line)
    return "\n".join(lines)


def run_tests(user_code: str, test_code: str, timeout_seconds: int = 2) -> dict:
    """Run user code and tests in a separate Python process.

    Returns a dict with keys: passed (bool), output (str), error (str).
    """
    normalized_tests = _normalize_tests(test_code)

    script_lines = [
        "import sys",
        "import traceback",
        "",
        "class ExpectationError(AssertionError):",
        "    def __init__(self, expected, actual):",
        "        message = f\"ожидалось: {expected}\\nваш код: {actual}\"",
        "        super().__init__(message)",
        "        self.expected = expected",
        "        self.actual = actual",
        "",
        "def expect(actual, expected):",
        "    if actual != expected:",
        "        raise ExpectationError(expected, actual)",
        "",
        f"USER_CODE = {user_code!r}",
        f"TEST_CODE = {normalized_tests!r}",
        "namespace = {}",
        "try:",
        "    exec(USER_CODE, namespace)",
        "except (SyntaxError, IndentationError) as exc:",
        "    print('Ошибка в коде:')",
        "    line = (exc.text or '').rstrip('\\n')",
        "    if exc.lineno:",
        "        print(f'Строка {exc.lineno}: {line}')",
        "    else:",
        "        print(f'Строка ?: {line}')",
        "    if getattr(exc, 'offset', None):",
        "        print(' ' * (exc.offset - 1) + '^')",
        "    msg = getattr(exc, 'msg', str(exc))",
        "    print(f'{exc.__class__.__name__}: {msg}')",
        "    sys.exit(1)",
        "except Exception:",
        "    print('Ошибка в коде:')",
        "    traceback.print_exc()",
        "    sys.exit(1)",
        "try:",
        "    namespace['expect'] = expect",
        "    namespace['ExpectationError'] = ExpectationError",
        "    exec(TEST_CODE, namespace)",
        "except ExpectationError as exc:",
        "    print(str(exc))",
        "    sys.exit(1)",
        "except Exception:",
        "    print('Тесты не пройдены:')",
        "    traceback.print_exc()",
        "    sys.exit(1)",
        "print('OK')",
    ]
    script = "\n".join(script_lines)

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as handle:
            handle.write(script)
            temp_path = handle.name

        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            env={
                "PATH": os.environ.get("PATH", ""),
                "PYTHONIOENCODING": "utf-8",
            },
        )
        output = (result.stdout or "").strip()
        error = (result.stderr or "").strip()
        passed = result.returncode == 0
        return {"passed": passed, "output": output, "error": error}
    except subprocess.TimeoutExpired:
        return {"passed": False, "output": "", "error": "Превышено время выполнения."}
    finally:
        if temp_path:
            try:
                os.remove(temp_path)
            except OSError:
                pass
