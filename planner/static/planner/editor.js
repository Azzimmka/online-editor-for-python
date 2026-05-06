(function () {
    "use strict";

    /* ═══════════════════════════════════════════════════════
       PYTHON KNOWLEDGE BASE
       ═══════════════════════════════════════════════════════ */

    /* ── Python keywords ───────────────────────────────── */
    var PYTHON_KEYWORDS = [
        "False", "None", "True", "and", "as", "assert", "async", "await",
        "break", "class", "continue", "def", "del", "elif", "else",
        "except", "finally", "for", "from", "global", "if", "import",
        "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise",
        "return", "try", "while", "with", "yield"
    ];

    /* ── Python built-in functions ─────────────────────── */
    var PYTHON_BUILTINS = [
        "abs", "all", "any", "ascii", "bin", "bool", "breakpoint",
        "bytearray", "bytes", "callable", "chr", "classmethod",
        "compile", "complex", "delattr", "dict", "dir", "divmod",
        "enumerate", "eval", "exec", "filter", "float", "format",
        "frozenset", "getattr", "globals", "hasattr", "hash", "help",
        "hex", "id", "input", "int", "isinstance", "issubclass",
        "iter", "len", "list", "locals", "map", "max", "memoryview",
        "min", "next", "object", "oct", "open", "ord", "pow", "print",
        "property", "range", "repr", "reversed", "round", "set",
        "setattr", "slice", "sorted", "staticmethod", "str", "sum",
        "super", "tuple", "type", "vars", "zip"
    ];

    /* ── Common exceptions ─────────────────────────────── */
    var PYTHON_EXCEPTIONS = [
        "Exception", "ValueError", "TypeError", "KeyError", "IndexError",
        "AttributeError", "NameError", "RuntimeError", "StopIteration",
        "ZeroDivisionError", "FileNotFoundError", "IOError", "OSError",
        "ImportError", "NotImplementedError", "RecursionError",
        "OverflowError", "ArithmeticError"
    ];

    /* ── Dunder methods ────────────────────────────────── */
    var DUNDER_METHODS = [
        { text: "__init__(self):", desc: "Конструктор" },
        { text: "__str__(self):", desc: "Строковое представление" },
        { text: "__repr__(self):", desc: "Отладочное представление" },
        { text: "__len__(self):", desc: "Длина объекта" },
        { text: "__getitem__(self, key):", desc: "Получение по индексу" },
        { text: "__setitem__(self, key, value):", desc: "Установка по индексу" },
        { text: "__contains__(self, item):", desc: "Оператор in" },
        { text: "__iter__(self):", desc: "Итератор" },
        { text: "__next__(self):", desc: "Следующий элемент" },
        { text: "__eq__(self, other):", desc: "Сравнение ==" },
        { text: "__lt__(self, other):", desc: "Сравнение <" },
        { text: "__le__(self, other):", desc: "Сравнение <=" },
        { text: "__gt__(self, other):", desc: "Сравнение >" },
        { text: "__add__(self, other):", desc: "Оператор +" },
        { text: "__sub__(self, other):", desc: "Оператор -" },
        { text: "__mul__(self, other):", desc: "Оператор *" },
        { text: "__call__(self):", desc: "Вызов как функция" },
        { text: "__enter__(self):", desc: "Контекстный менеджер вход" },
        { text: "__exit__(self, exc_type, exc_val, exc_tb):", desc: "Контекстный менеджер выход" },
        { text: "__hash__(self):", desc: "Хэш объекта" },
        { text: "__bool__(self):", desc: "Приведение к bool" }
    ];

    /* ── Methods by type ──────────────────────────────── */
    var METHODS = {
        str: [
            "capitalize", "casefold", "center", "count", "encode",
            "endswith", "expandtabs", "find", "format", "format_map",
            "index", "isalnum", "isalpha", "isascii", "isdecimal",
            "isdigit", "isidentifier", "islower", "isnumeric",
            "isprintable", "isspace", "istitle", "isupper", "join",
            "ljust", "lower", "lstrip", "maketrans", "partition",
            "removeprefix", "removesuffix", "replace", "rfind",
            "rindex", "rjust", "rpartition", "rsplit", "rstrip",
            "split", "splitlines", "startswith", "strip", "swapcase",
            "title", "translate", "upper", "zfill"
        ],
        list: [
            "append", "clear", "copy", "count", "extend", "index",
            "insert", "pop", "remove", "reverse", "sort"
        ],
        dict: [
            "clear", "copy", "fromkeys", "get", "items", "keys",
            "pop", "popitem", "setdefault", "update", "values"
        ],
        set: [
            "add", "clear", "copy", "difference", "difference_update",
            "discard", "intersection", "intersection_update",
            "isdisjoint", "issubset", "issuperset", "pop", "remove",
            "symmetric_difference", "symmetric_difference_update",
            "union", "update"
        ]
    };

    /* Flat unique method list */
    var ALL_METHODS = [];
    (function () {
        var seen = {};
        for (var type in METHODS) {
            for (var i = 0; i < METHODS[type].length; i++) {
                var m = METHODS[type][i];
                if (!seen[m]) { seen[m] = true; ALL_METHODS.push(m); }
            }
        }
        ALL_METHODS.sort();
    })();

    /* ═══════════════════════════════════════════════════════
       SMART SNIPPETS
       ═══════════════════════════════════════════════════════ */
    var SNIPPETS = {
        "def": {
            template: "def ${1:name}(${2:}):\n    ${3:pass}",
            desc: "Функция"
        },
        "class": {
            template: "class ${1:Name}:\n    def __init__(self${2:}):\n        ${3:pass}",
            desc: "Класс"
        },
        "for": {
            template: "for ${1:item} in ${2:items}:\n    ${3:pass}",
            desc: "Цикл for"
        },
        "while": {
            template: "while ${1:condition}:\n    ${2:pass}",
            desc: "Цикл while"
        },
        "if": {
            template: "if ${1:condition}:\n    ${2:pass}",
            desc: "Условие if"
        },
        "ife": {
            template: "if ${1:condition}:\n    ${2:pass}\nelse:\n    ${3:pass}",
            desc: "if / else"
        },
        "elif": {
            template: "elif ${1:condition}:\n    ${2:pass}",
            desc: "elif блок"
        },
        "try": {
            template: "try:\n    ${1:pass}\nexcept ${2:Exception} as e:\n    ${3:pass}",
            desc: "try / except"
        },
        "tryf": {
            template: "try:\n    ${1:pass}\nexcept ${2:Exception} as e:\n    ${3:pass}\nfinally:\n    ${4:pass}",
            desc: "try / except / finally"
        },
        "with": {
            template: "with ${1:expr} as ${2:var}:\n    ${3:pass}",
            desc: "Контекстный менеджер"
        },
        "lc": {
            template: "[${1:x} for ${2:x} in ${3:items}]",
            desc: "List comprehension"
        },
        "dc": {
            template: "{${1:k}: ${2:v} for ${1:k}, ${2:v} in ${3:items}}",
            desc: "Dict comprehension"
        },
        "sc": {
            template: "{${1:x} for ${2:x} in ${3:items}}",
            desc: "Set comprehension"
        },
        "main": {
            template: "if __name__ == \"__main__\":\n    ${1:pass}",
            desc: "Точка входа"
        },
        "pr": {
            template: "print(${1:})",
            desc: "print()"
        },
        "ret": {
            template: "return ${1:}",
            desc: "return"
        },
        "lam": {
            template: "lambda ${1:x}: ${2:x}",
            desc: "Lambda функция"
        },
        "init": {
            template: "def __init__(self${1:}):\n    ${2:pass}",
            desc: "__init__ метод"
        }
    };

    /* Expand snippet: replace ${N:default} placeholders */
    function expandSnippet(cm, snippet, indent) {
        var lines = snippet.template.split("\n");
        var result = [];
        for (var i = 0; i < lines.length; i++) {
            result.push(i === 0 ? lines[i] : indent + lines[i]);
        }
        var text = result.join("\n");

        /* Remove placeholder markers, keep defaults */
        var firstCursorPos = null;
        var cleaned = "";
        var col = 0;
        var lineNum = 0;

        /* Simple placeholder removal: ${N:text} → text */
        text = text.replace(/\$\{(\d+):([^}]*)\}/g, function (match, num, defaultVal, offset) {
            if (!firstCursorPos && num === "1") {
                /* Calculate position of first placeholder */
                var before = text.substring(0, offset).replace(/\$\{(\d+):([^}]*)\}/g, "$2");
                var blines = before.split("\n");
                firstCursorPos = {
                    line: blines.length - 1,
                    ch: blines[blines.length - 1].length
                };
            }
            return defaultVal;
        });

        return { text: text, cursor: firstCursorPos };
    }

    /* ═══════════════════════════════════════════════════════
       CODE ANALYSIS
       ═══════════════════════════════════════════════════════ */

    /* Extract user-defined names with context */
    function analyzeCode(code) {
        var names = {};
        var selfAttrs = [];
        var classes = [];
        var functions = [];
        var variables = [];
        var lines = code.split("\n");
        var currentClass = null;

        for (var i = 0; i < lines.length; i++) {
            var line = lines[i];
            var trimmed = line.replace(/^\s+/, "");
            var indentLevel = line.length - line.replace(/^\s+/, "").length;

            /* Track current class scope */
            var classMatch = line.match(/^class\s+([a-zA-Z_]\w*)/);
            if (classMatch) {
                currentClass = classMatch[1];
                classes.push(currentClass);
                names[classMatch[1]] = "class";
            }

            /* Exit class if dedented to top level */
            if (indentLevel === 0 && !classMatch && currentClass && trimmed.length > 0) {
                currentClass = null;
            }

            /* def function_name( */
            var defMatch = line.match(/\bdef\s+([a-zA-Z_]\w*)/);
            if (defMatch) {
                names[defMatch[1]] = currentClass ? "method" : "function";
                if (!currentClass) functions.push(defMatch[1]);
            }

            /* self.attr = ... inside class */
            var selfMatch = line.match(/\bself\.([a-zA-Z_]\w*)\s*=/);
            if (selfMatch && selfAttrs.indexOf(selfMatch[1]) === -1) {
                selfAttrs.push(selfMatch[1]);
            }

            /* Also capture self.attr references (not just assignments) */
            var selfRefs = line.match(/\bself\.([a-zA-Z_]\w*)/g);
            if (selfRefs) {
                for (var sr = 0; sr < selfRefs.length; sr++) {
                    var attrName = selfRefs[sr].replace("self.", "");
                    if (selfAttrs.indexOf(attrName) === -1) {
                        selfAttrs.push(attrName);
                    }
                }
            }

            /* variable = ... */
            var varMatch = line.match(/^[ \t]*([a-zA-Z_]\w*)\s*=[^=]/);
            if (varMatch && PYTHON_KEYWORDS.indexOf(varMatch[1]) === -1 && varMatch[1] !== "self") {
                names[varMatch[1]] = "variable";
                variables.push(varMatch[1]);
            }

            /* for x in ... */
            var forMatch = line.match(/\bfor\s+([a-zA-Z_]\w*)\s+in\b/);
            if (forMatch) {
                names[forMatch[1]] = "variable";
            }

            /* function parameters */
            if (defMatch) {
                var paramsMatch = line.match(/\bdef\s+\w+\s*\(([^)]*)\)/);
                if (paramsMatch) {
                    var params = paramsMatch[1].split(",");
                    for (var p = 0; p < params.length; p++) {
                        var param = params[p].trim().split("=")[0].split(":")[0].trim();
                        if (param && param !== "self" && param !== "cls") {
                            names[param] = "parameter";
                        }
                    }
                }
            }
        }

        return {
            names: names,
            selfAttrs: selfAttrs,
            classes: classes,
            functions: functions,
            variables: variables,
            currentClass: currentClass
        };
    }

    /* ── Detect if cursor is inside a class body ───────── */
    function isInsideClass(cm, line) {
        for (var i = line; i >= 0; i--) {
            var text = cm.getLine(i);
            if (/^class\s+/.test(text)) return true;
            if (i < line && /^\S/.test(text) && !/^class\s+/.test(text) && text.trim().length > 0) {
                return false;
            }
        }
        return false;
    }

    /* ── Detect if cursor is inside a def body ─────────── */
    function isInsideDef(cm, line) {
        for (var i = line; i >= 0; i--) {
            var text = cm.getLine(i);
            if (/\bdef\s+/.test(text)) return true;
            if (i < line && /^\S/.test(text.trim()) && text.trim().length > 0) return false;
        }
        return false;
    }

    /* ═══════════════════════════════════════════════════════
       SYNTAX ERROR CHECKING
       ═══════════════════════════════════════════════════════ */
    var errorWidgets = [];
    var errorCheckTimeout = null;

    function clearErrors(cm) {
        for (var i = 0; i < errorWidgets.length; i++) {
            cm.removeLineWidget(errorWidgets[i]);
        }
        errorWidgets = [];

        /* Clear line error markers */
        for (var j = 0; j < cm.lineCount(); j++) {
            cm.removeLineClass(j, "background", "cm-error-line");
        }
    }

    function checkSyntax(cm) {
        clearErrors(cm);
        var code = cm.getValue();
        if (!code.trim()) return;

        /* Check common syntax errors client-side */
        var lines = code.split("\n");
        var parenStack = [];
        var bracketStack = [];
        var braceStack = [];
        var inString = false;
        var stringChar = "";
        var inTriple = false;

        for (var i = 0; i < lines.length; i++) {
            var line = lines[i];
            var trimmed = line.trim();

            /* Skip empty lines and comments */
            if (!trimmed || trimmed.charAt(0) === "#") continue;

            /* Check for obvious indentation errors: content after colon on same line is OK,
               but next line should be indented if current ends with colon */
            if (i > 0) {
                var prevLine = lines[i - 1].trimEnd();
                var prevTrimmed = prevLine.trim();
                if (prevTrimmed.endsWith(":") && !prevTrimmed.startsWith("#")) {
                    var prevIndent = prevLine.length - prevLine.replace(/^\s+/, "").length;
                    var currIndent = line.length - line.replace(/^\s+/, "").length;
                    if (trimmed.length > 0 && currIndent <= prevIndent) {
                        showError(cm, i, "Ожидается отступ после ':'");
                    }
                }
            }

            /* Check mismatched brackets (simplified) */
            for (var c = 0; c < line.length; c++) {
                var ch = line.charAt(c);
                if (ch === "#" && !inString) break; /* rest is comment */
                if ((ch === '"' || ch === "'") && !inString) {
                    inString = true;
                    stringChar = ch;
                    /* Check for triple quotes */
                    if (line.substring(c, c + 3) === ch + ch + ch) {
                        inTriple = true;
                        c += 2;
                    }
                    continue;
                }
                if (inString) {
                    if (inTriple) {
                        if (line.substring(c, c + 3) === stringChar + stringChar + stringChar) {
                            inString = false;
                            inTriple = false;
                            c += 2;
                        }
                    } else if (ch === stringChar && (c === 0 || line.charAt(c - 1) !== "\\")) {
                        inString = false;
                    }
                    continue;
                }
                if (ch === "(") parenStack.push({ line: i, ch: c });
                if (ch === "[") bracketStack.push({ line: i, ch: c });
                if (ch === "{") braceStack.push({ line: i, ch: c });
                if (ch === ")") { if (!parenStack.length) showError(cm, i, "Лишняя закрывающая ')'"); else parenStack.pop(); }
                if (ch === "]") { if (!bracketStack.length) showError(cm, i, "Лишняя закрывающая ']'"); else bracketStack.pop(); }
                if (ch === "}") { if (!braceStack.length) showError(cm, i, "Лишняя закрывающая '}'"); else braceStack.pop(); }
            }
        }

        /* Report unclosed brackets */
        if (parenStack.length) showError(cm, parenStack[parenStack.length - 1].line, "Незакрытая скобка '('");
        if (bracketStack.length) showError(cm, bracketStack[bracketStack.length - 1].line, "Незакрытая скобка '['");
        if (braceStack.length) showError(cm, braceStack[braceStack.length - 1].line, "Незакрытая скобка '{'");
    }

    function showError(cm, lineNum, message) {
        cm.addLineClass(lineNum, "background", "cm-error-line");

        var widget = document.createElement("div");
        widget.className = "cm-error-widget";
        widget.textContent = "⚠ " + message;

        var w = cm.addLineWidget(lineNum, widget, { coverGutter: false, noHScroll: true, above: false });
        errorWidgets.push(w);
    }

    /* ═══════════════════════════════════════════════════════
       HINT SYSTEM
       ═══════════════════════════════════════════════════════ */

    function hintClass(kind) {
        switch (kind) {
            case "keyword": return "hint-keyword";
            case "builtin": return "hint-builtin";
            case "method": return "hint-method";
            case "function": return "hint-function";
            case "class": return "hint-class";
            case "variable": return "hint-variable";
            case "parameter": return "hint-parameter";
            case "snippet": return "hint-snippet";
            case "attr": return "hint-variable";
            case "dunder": return "hint-method";
            case "exception": return "hint-class";
            default: return "hint-other";
        }
    }

    function makeHint(text, kind, displayExtra) {
        var hint = {
            text: text,
            displayText: text,
            className: hintClass(kind),
            _kind: kind
        };
        if (displayExtra) {
            hint.displayText = text + "  " + displayExtra;
        }
        return hint;
    }

    /* ── Main hint function ────────────────────────────── */
    function pythonHint(cm) {
        var cur = cm.getCursor();
        var token = cm.getTokenAt(cur);
        var code = cm.getValue();
        var lineContent = cm.getLine(cur.line);
        var beforeCursor = lineContent.slice(0, cur.ch);

        /* ── self. completion ── */
        var selfDotMatch = beforeCursor.match(/\bself\.(\w*)$/);
        if (selfDotMatch) {
            var partial = selfDotMatch[1].toLowerCase();
            var analysis = analyzeCode(code);
            var list = [];

            /* Self attributes */
            for (var sa = 0; sa < analysis.selfAttrs.length; sa++) {
                var attr = analysis.selfAttrs[sa];
                if (attr.toLowerCase().indexOf(partial) === 0) {
                    list.push(makeHint(attr, "attr"));
                }
            }

            /* Dunder methods if inside class */
            if (isInsideClass(cm, cur.line)) {
                for (var d = 0; d < DUNDER_METHODS.length; d++) {
                    var dm = DUNDER_METHODS[d];
                    var methodName = dm.text.split("(")[0];
                    if (methodName.toLowerCase().indexOf(partial) === 0) {
                        list.push(makeHint(methodName, "dunder", dm.desc));
                    }
                }
            }

            if (list.length === 0) return null;
            return {
                list: list,
                from: CodeMirror.Pos(cur.line, cur.ch - selfDotMatch[1].length),
                to: cur
            };
        }

        /* ── Dot completion (methods) ── */
        var dotMatch = beforeCursor.match(/\.(\w*)$/);
        if (dotMatch) {
            var dotPartial = dotMatch[1].toLowerCase();
            var dotList = [];
            for (var mi = 0; mi < ALL_METHODS.length; mi++) {
                if (ALL_METHODS[mi].toLowerCase().indexOf(dotPartial) === 0) {
                    dotList.push(makeHint(ALL_METHODS[mi], "method"));
                }
            }
            if (dotList.length === 0) return null;
            return {
                list: dotList,
                from: CodeMirror.Pos(cur.line, cur.ch - dotMatch[1].length),
                to: cur
            };
        }

        /* ── Regular word completion ── */
        var word = "";
        var match = beforeCursor.match(/([a-zA-Z_]\w*)$/);
        if (match) word = match[1];
        if (word.length < 1) return null;

        var lower = word.toLowerCase();
        var results = [];
        var seen = {};
        var codeAnalysis = analyzeCode(code);

        /* ── Snippets (highest priority) ── */
        for (var snippetKey in SNIPPETS) {
            if (snippetKey.indexOf(lower) === 0 && snippetKey !== word) {
                var snip = SNIPPETS[snippetKey];
                var snippetHint = makeHint(snippetKey, "snippet", "→ " + snip.desc);
                /* Custom hint handler for snippets */
                (function (sk) {
                    snippetHint.hint = function (cm, data, completion) {
                        var from = data.from;
                        var to = data.to;
                        var indentStr = "";
                        var ln = cm.getLine(from.line);
                        var indentMatch = ln.match(/^(\s*)/);
                        if (indentMatch) indentStr = indentMatch[1];

                        var expanded = expandSnippet(cm, SNIPPETS[sk], indentStr);
                        cm.replaceRange(expanded.text, from, to);

                        if (expanded.cursor) {
                            cm.setCursor(CodeMirror.Pos(
                                from.line + expanded.cursor.line,
                                (expanded.cursor.line === 0 ? from.ch : 0) +
                                    expanded.cursor.ch - sk.length
                            ));
                        }
                    };
                })(snippetKey);
                results.push(snippetHint);
                seen[snippetKey] = true;
            }
        }

        /* ── Dunder methods if inside class and typing "def __" ── */
        if (isInsideClass(cm, cur.line) && (lower.indexOf("__") === 0 || lower === "def")) {
            for (var di = 0; di < DUNDER_METHODS.length; di++) {
                var dunder = DUNDER_METHODS[di];
                var fullDef = "def " + dunder.text;
                var dunderName = dunder.text.split("(")[0];
                if (dunderName.indexOf(lower) === 0 && !seen[dunderName]) {
                    results.push(makeHint(dunderName, "dunder", dunder.desc));
                    seen[dunderName] = true;
                }
            }
        }

        /* ── User-defined names ── */
        for (var name in codeAnalysis.names) {
            if (!seen[name] && name.toLowerCase().indexOf(lower) === 0 && name !== word) {
                results.push(makeHint(name, codeAnalysis.names[name]));
                seen[name] = true;
            }
        }

        /* ── Keywords ── */
        for (var k = 0; k < PYTHON_KEYWORDS.length; k++) {
            var kw = PYTHON_KEYWORDS[k];
            if (!seen[kw] && kw.toLowerCase().indexOf(lower) === 0 && kw !== word) {
                results.push(makeHint(kw, "keyword"));
                seen[kw] = true;
            }
        }

        /* ── Built-in functions ── */
        for (var b = 0; b < PYTHON_BUILTINS.length; b++) {
            var bf = PYTHON_BUILTINS[b];
            if (!seen[bf] && bf.toLowerCase().indexOf(lower) === 0 && bf !== word) {
                results.push(makeHint(bf, "builtin"));
                seen[bf] = true;
            }
        }

        /* ── Exceptions (if after 'except' or 'raise') ── */
        if (/\b(except|raise)\s*$/.test(beforeCursor.replace(/\w+$/, "").trim()) ||
            /\b(except|raise)\s+\w*$/.test(beforeCursor)) {
            for (var ei = 0; ei < PYTHON_EXCEPTIONS.length; ei++) {
                var exc = PYTHON_EXCEPTIONS[ei];
                if (!seen[exc] && exc.toLowerCase().indexOf(lower) === 0) {
                    results.push(makeHint(exc, "exception"));
                    seen[exc] = true;
                }
            }
        }

        if (results.length === 0) return null;

        return {
            list: results,
            from: CodeMirror.Pos(cur.line, cur.ch - word.length),
            to: cur
        };
    }

    /* ═══════════════════════════════════════════════════════
       SMART INDENTATION
       ═══════════════════════════════════════════════════════ */

    /* Auto-dedent keywords: after typing these, reduce indent */
    var DEDENT_KEYWORDS = ["return", "break", "continue", "pass", "raise"];

    function smartNewline(cm) {
        var cur = cm.getCursor();
        var line = cm.getLine(cur.line);
        var trimmed = line.trim();
        var indent = line.match(/^(\s*)/)[1];

        /* If line ends with ':', add extra indent */
        if (trimmed.endsWith(":") && !trimmed.startsWith("#")) {
            cm.replaceSelection("\n" + indent + "    ");
            return;
        }

        /* If current line is a dedent keyword, reduce indent on NEXT line */
        for (var i = 0; i < DEDENT_KEYWORDS.length; i++) {
            var kw = DEDENT_KEYWORDS[i];
            if (trimmed.startsWith(kw + " ") || trimmed === kw ||
                trimmed.startsWith(kw + "(")) {
                var reduced = indent.length >= 4 ? indent.slice(4) : indent;
                cm.replaceSelection("\n" + reduced);
                return;
            }
        }

        /* Default: maintain current indent */
        cm.replaceSelection("\n" + indent);
    }

    /* ═══════════════════════════════════════════════════════
       FORM SUBMIT HELPER
       ═══════════════════════════════════════════════════════ */
    function submitForm(form) {
        if (!form) return;
        if (typeof form.requestSubmit === "function") {
            form.requestSubmit();
        } else {
            form.submit();
        }
    }

    /* ═══════════════════════════════════════════════════════
       EDITOR INITIALIZATION
       ═══════════════════════════════════════════════════════ */
    function initEditors() {
        if (typeof CodeMirror === "undefined") return;

        var textareas = document.querySelectorAll("textarea.code-editor");
        if (!textareas.length) return;

        textareas.forEach(function (textarea) {
            if (textarea.dataset.cmReady === "true") return;

            var form = textarea.closest("form");
            var shell = textarea.closest(".editor-shell");
            var draftBar = shell ? shell.querySelector(".draft-bar") : null;
            var starterField = shell ? shell.querySelector(".starter-code") : null;
            var starterValue = starterField ? starterField.value : textarea.value;
            var taskId = textarea.dataset.taskId || (shell && shell.dataset.taskId) || "default";
            var draftKey = "draft:" + taskId;

            var cm = CodeMirror.fromTextArea(textarea, {
                mode: "python",
                lineNumbers: true,
                indentUnit: 4,
                tabSize: 4,
                indentWithTabs: false,
                lineWrapping: true,
                autoCloseBrackets: true,
                matchBrackets: true,
                styleActiveLine: true,
                foldGutter: true,
                viewportMargin: Infinity,
                hintOptions: {
                    hint: pythonHint,
                    completeSingle: false,
                    alignWithWord: true,
                    closeOnUnfocus: true
                },
                extraKeys: {
                    "Enter": function (cmInstance) {
                        if (cmInstance.state.completionActive) {
                            /* Let hint system handle Enter */
                            return CodeMirror.Pass;
                        }
                        smartNewline(cmInstance);
                    },
                    "Ctrl-Enter": function () { submitForm(form); },
                    "Cmd-Enter": function () { submitForm(form); },
                    "Ctrl-/": "toggleComment",
                    "Cmd-/": "toggleComment",
                    "Ctrl-Space": function (cmInstance) {
                        cmInstance.showHint({ hint: pythonHint });
                    },
                    "Cmd-Space": function () { /* macOS Spotlight */ },
                    "Ctrl-D": function (cmInstance) {
                        /* Duplicate line */
                        var cursor = cmInstance.getCursor();
                        var lineContent = cmInstance.getLine(cursor.line);
                        cmInstance.replaceRange(
                            "\n" + lineContent,
                            CodeMirror.Pos(cursor.line)
                        );
                        cmInstance.setCursor(CodeMirror.Pos(cursor.line + 1, cursor.ch));
                    },
                    "Alt-Up": function (cmInstance) {
                        /* Move line up */
                        var cursor = cmInstance.getCursor();
                        if (cursor.line === 0) return;
                        var currentLine = cmInstance.getLine(cursor.line);
                        var prevLine = cmInstance.getLine(cursor.line - 1);
                        cmInstance.replaceRange(currentLine,
                            CodeMirror.Pos(cursor.line - 1, 0),
                            CodeMirror.Pos(cursor.line - 1, prevLine.length));
                        cmInstance.replaceRange(prevLine,
                            CodeMirror.Pos(cursor.line, 0),
                            CodeMirror.Pos(cursor.line, currentLine.length));
                        cmInstance.setCursor(CodeMirror.Pos(cursor.line - 1, cursor.ch));
                    },
                    "Alt-Down": function (cmInstance) {
                        /* Move line down */
                        var cursor = cmInstance.getCursor();
                        if (cursor.line >= cmInstance.lineCount() - 1) return;
                        var currentLine = cmInstance.getLine(cursor.line);
                        var nextLine = cmInstance.getLine(cursor.line + 1);
                        cmInstance.replaceRange(nextLine,
                            CodeMirror.Pos(cursor.line, 0),
                            CodeMirror.Pos(cursor.line, currentLine.length));
                        cmInstance.replaceRange(currentLine,
                            CodeMirror.Pos(cursor.line + 1, 0),
                            CodeMirror.Pos(cursor.line + 1, nextLine.length));
                        cmInstance.setCursor(CodeMirror.Pos(cursor.line + 1, cursor.ch));
                    },
                    "Tab": function (cmInstance) {
                        /* If hint is active, accept it */
                        if (cmInstance.state.completionActive) {
                            return CodeMirror.Pass;
                        }

                        /* Check for snippet expansion */
                        var cursor = cmInstance.getCursor();
                        var lineBefore = cmInstance.getLine(cursor.line).slice(0, cursor.ch);
                        var wordMatch = lineBefore.match(/([a-zA-Z_]\w*)$/);
                        if (wordMatch && SNIPPETS[wordMatch[1]]) {
                            var snippetKey = wordMatch[1];
                            var indentStr = lineBefore.match(/^(\s*)/)[1];
                            var expanded = expandSnippet(cm, SNIPPETS[snippetKey], indentStr);
                            var from = CodeMirror.Pos(cursor.line, cursor.ch - snippetKey.length);
                            cmInstance.replaceRange(expanded.text, from, cursor);
                            return;
                        }

                        if (cmInstance.somethingSelected()) {
                            cmInstance.indentSelection("add");
                        } else {
                            cmInstance.execCommand("insertSoftTab");
                        }
                    },
                    "Shift-Tab": function (cmInstance) {
                        cmInstance.indentSelection("subtract");
                    }
                }
            });

            /* ── Auto-trigger hints on typing ── */
            var hintTimeout = null;
            cm.on("inputRead", function (cmInstance, change) {
                if (change.origin !== "+input") return;
                var ch = change.text[0];
                if (!ch) return;

                /* Trigger on dot immediately */
                if (ch === ".") {
                    clearTimeout(hintTimeout);
                    hintTimeout = setTimeout(function () {
                        if (!cmInstance.state.completionActive) {
                            cmInstance.showHint({ hint: pythonHint });
                        }
                    }, 80);
                    return;
                }

                /* Trigger on letter/underscore after typing 2+ chars */
                if (/[a-zA-Z_]/.test(ch)) {
                    clearTimeout(hintTimeout);
                    hintTimeout = setTimeout(function () {
                        var cur = cmInstance.getCursor();
                        var line = cmInstance.getLine(cur.line);
                        var before = line.slice(0, cur.ch);
                        var wordMatch = before.match(/([a-zA-Z_]\w*)$/);
                        if (wordMatch && wordMatch[1].length >= 2) {
                            if (!cmInstance.state.completionActive) {
                                cmInstance.showHint({ hint: pythonHint });
                            }
                        }
                    }, 200);
                }
            });

            /* ── Syntax checking with debounce ── */
            cm.on("change", function () {
                textarea.value = cm.getValue();
                updateStats();

                /* Save draft */
                try { localStorage.setItem(draftKey, cm.getValue()); }
                catch (e) { /* ignore */ }

                /* Debounced syntax check */
                clearTimeout(errorCheckTimeout);
                errorCheckTimeout = setTimeout(function () {
                    checkSyntax(cm);
                }, 800);
            });

            /* ── Stats ── */
            var statsLines = shell ? shell.querySelector("[data-stat='lines']") : null;
            var statsChars = shell ? shell.querySelector("[data-stat='chars']") : null;

            function updateStats() {
                var value = cm.getValue();
                if (statsLines) statsLines.textContent = "Строк: " + value.split("\n").length;
                if (statsChars) statsChars.textContent = "Символов: " + value.length;
            }

            /* ── Draft ── */
            function showDraftBar() { if (draftBar) draftBar.hidden = false; }
            function hideDraftBar() { if (draftBar) draftBar.hidden = true; }

            var savedDraft = null;
            try { savedDraft = localStorage.getItem(draftKey); }
            catch (e) { savedDraft = null; }

            if (savedDraft && savedDraft !== textarea.value) {
                showDraftBar();
            }

            /* ── Toolbar actions ── */
            if (shell) {
                shell.addEventListener("click", function (event) {
                    var target = event.target;
                    while (target && target !== shell && !target.dataset.action) {
                        target = target.parentElement;
                    }
                    if (!target || !target.dataset) return;

                    var action = target.dataset.action;
                    if (!action) return;
                    event.preventDefault();

                    if (action === "copy") {
                        var text = cm.getValue();
                        if (navigator.clipboard && navigator.clipboard.writeText) {
                            navigator.clipboard.writeText(text).catch(function () {});
                        }
                        return;
                    }

                    if (action === "reset") {
                        cm.setValue(starterValue || "");
                        cm.focus();
                        return;
                    }

                    if (action === "restore-draft") {
                        if (savedDraft) {
                            cm.setValue(savedDraft);
                            cm.focus();
                        }
                        hideDraftBar();
                        return;
                    }

                    if (action === "clear-draft") {
                        try { localStorage.removeItem(draftKey); }
                        catch (e) { /* ignore */ }
                        hideDraftBar();
                    }
                });
            }

            /* Initial stats & syntax check */
            updateStats();
            setTimeout(function () { checkSyntax(cm); }, 500);
            textarea.dataset.cmReady = "true";
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initEditors);
    } else {
        initEditors();
    }
})();
