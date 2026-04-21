(function () {
    /* ── Python built-in keywords ───────────────────────── */
    var PYTHON_KEYWORDS = [
        "False", "None", "True", "and", "as", "assert", "async", "await",
        "break", "class", "continue", "def", "del", "elif", "else",
        "except", "finally", "for", "from", "global", "if", "import",
        "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise",
        "return", "try", "while", "with", "yield"
    ];

    /* ── Python built-in functions ──────────────────────── */
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

    /* ── Common methods by type ─────────────────────────── */
    var METHODS = {
        // string methods
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
        // list methods
        list: [
            "append", "clear", "copy", "count", "extend", "index",
            "insert", "pop", "remove", "reverse", "sort"
        ],
        // dict methods
        dict: [
            "clear", "copy", "fromkeys", "get", "items", "keys",
            "pop", "popitem", "setdefault", "update", "values"
        ],
        // set methods
        set: [
            "add", "clear", "copy", "difference", "difference_update",
            "discard", "intersection", "intersection_update",
            "isdisjoint", "issubset", "issuperset", "pop", "remove",
            "symmetric_difference", "symmetric_difference_update",
            "union", "update"
        ]
    };

    /* Gather all methods into a flat unique list for dot-completion */
    var ALL_METHODS = [];
    (function () {
        var seen = {};
        for (var type in METHODS) {
            for (var i = 0; i < METHODS[type].length; i++) {
                var m = METHODS[type][i];
                if (!seen[m]) {
                    seen[m] = true;
                    ALL_METHODS.push(m);
                }
            }
        }
        ALL_METHODS.sort();
    })();

    /* ── Extract user-defined names from code ──────────── */
    function extractUserNames(code) {
        var names = {};
        var lines = code.split("\n");
        for (var i = 0; i < lines.length; i++) {
            var line = lines[i];

            // def function_name(
            var defMatch = line.match(/\bdef\s+([a-zA-Z_]\w*)/);
            if (defMatch) names[defMatch[1]] = "function";

            // class ClassName
            var classMatch = line.match(/\bclass\s+([a-zA-Z_]\w*)/);
            if (classMatch) names[classMatch[1]] = "class";

            // variable = ...
            var varMatch = line.match(/^[ \t]*([a-zA-Z_]\w*)\s*=[^=]/);
            if (varMatch && PYTHON_KEYWORDS.indexOf(varMatch[1]) === -1) {
                names[varMatch[1]] = "variable";
            }

            // for x in ...
            var forMatch = line.match(/\bfor\s+([a-zA-Z_]\w*)\s+in\b/);
            if (forMatch) names[forMatch[1]] = "variable";

            // function parameters: def foo(a, b, c):
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
        return names;
    }

    /* ── Determine hint type icon/label ────────────────── */
    function hintClass(kind) {
        switch (kind) {
            case "keyword": return "hint-keyword";
            case "builtin": return "hint-builtin";
            case "method": return "hint-method";
            case "function": return "hint-function";
            case "class": return "hint-class";
            case "variable": return "hint-variable";
            case "parameter": return "hint-parameter";
            default: return "hint-other";
        }
    }

    function makeHint(text, kind) {
        return {
            text: text,
            displayText: text,
            className: hintClass(kind),
            _kind: kind
        };
    }

    /* ── Custom Python hint function ───────────────────── */
    function pythonHint(cm) {
        var cur = cm.getCursor();
        var token = cm.getTokenAt(cur);
        var code = cm.getValue();

        /* Check if we're after a dot — show methods */
        var lineContent = cm.getLine(cur.line);
        var beforeCursor = lineContent.slice(0, cur.ch);
        var dotMatch = beforeCursor.match(/\.(\w*)$/);

        if (dotMatch) {
            var partial = dotMatch[1].toLowerCase();
            var list = [];
            for (var i = 0; i < ALL_METHODS.length; i++) {
                if (ALL_METHODS[i].toLowerCase().indexOf(partial) === 0) {
                    list.push(makeHint(ALL_METHODS[i], "method"));
                }
            }
            if (list.length === 0) return null;
            return {
                list: list,
                from: CodeMirror.Pos(cur.line, cur.ch - dotMatch[1].length),
                to: cur
            };
        }

        /* Regular word completion */
        var word = "";
        if (token.type === "variable" || token.type === "keyword" || token.type === "builtin" ||
            token.type === "def" || token.type === null) {
            var match = beforeCursor.match(/([a-zA-Z_]\w*)$/);
            if (match) word = match[1];
        }

        if (word.length < 1) return null;

        var lower = word.toLowerCase();
        var results = [];
        var seen = {};

        /* User-defined names first */
        var userNames = extractUserNames(code);
        for (var name in userNames) {
            if (name.toLowerCase().indexOf(lower) === 0 && name !== word) {
                results.push(makeHint(name, userNames[name]));
                seen[name] = true;
            }
        }

        /* Keywords */
        for (var k = 0; k < PYTHON_KEYWORDS.length; k++) {
            var kw = PYTHON_KEYWORDS[k];
            if (!seen[kw] && kw.toLowerCase().indexOf(lower) === 0 && kw !== word) {
                results.push(makeHint(kw, "keyword"));
                seen[kw] = true;
            }
        }

        /* Built-in functions */
        for (var b = 0; b < PYTHON_BUILTINS.length; b++) {
            var bf = PYTHON_BUILTINS[b];
            if (!seen[bf] && bf.toLowerCase().indexOf(lower) === 0 && bf !== word) {
                results.push(makeHint(bf, "builtin"));
                seen[bf] = true;
            }
        }

        if (results.length === 0) return null;

        return {
            list: results,
            from: CodeMirror.Pos(cur.line, cur.ch - word.length),
            to: cur
        };
    }

    /* ── Submit form helper ────────────────────────────── */
    function submitForm(form) {
        if (!form) return;
        if (typeof form.requestSubmit === "function") {
            form.requestSubmit();
        } else {
            form.submit();
        }
    }

    /* ── Initialize editors ────────────────────────────── */
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
                viewportMargin: Infinity,
                hintOptions: {
                    hint: pythonHint,
                    completeSingle: false,
                    alignWithWord: true,
                    closeOnUnfocus: true
                },
                extraKeys: {
                    "Ctrl-Enter": function () {
                        submitForm(form);
                    },
                    "Cmd-Enter": function () {
                        submitForm(form);
                    },
                    "Ctrl-/": "toggleComment",
                    "Ctrl-Space": function (cmInstance) {
                        cmInstance.showHint({ hint: pythonHint });
                    },
                    "Cmd-Space": function () {
                        /* macOS uses Cmd-Space for Spotlight, skip */
                    },
                    "Tab": function (cmInstance) {
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

            /* Auto-trigger hints on typing */
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

            /* ── Stats ── */
            var statsLines = shell ? shell.querySelector("[data-stat='lines']") : null;
            var statsChars = shell ? shell.querySelector("[data-stat='chars']") : null;

            function updateStats() {
                var value = cm.getValue();
                if (statsLines) {
                    statsLines.textContent = "Строк: " + value.split("\n").length;
                }
                if (statsChars) {
                    statsChars.textContent = "Символов: " + value.length;
                }
            }

            /* ── Draft ── */
            function showDraftBar() {
                if (draftBar) draftBar.hidden = false;
            }

            function hideDraftBar() {
                if (draftBar) draftBar.hidden = true;
            }

            var savedDraft = null;
            try {
                savedDraft = localStorage.getItem(draftKey);
            } catch (error) {
                savedDraft = null;
            }

            if (savedDraft && savedDraft !== textarea.value) {
                showDraftBar();
            }

            cm.on("change", function () {
                textarea.value = cm.getValue();
                updateStats();
                try {
                    localStorage.setItem(draftKey, cm.getValue());
                } catch (error) {
                    return;
                }
            });

            /* ── Toolbar actions ── */
            if (shell) {
                shell.addEventListener("click", function (event) {
                    var target = event.target;
                    /* Traverse up to find data-action (for SVG clicks) */
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
                        try {
                            localStorage.removeItem(draftKey);
                        } catch (error) {
                            return;
                        }
                        hideDraftBar();
                    }
                });
            }

            updateStats();
            textarea.dataset.cmReady = "true";
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initEditors);
    } else {
        initEditors();
    }
})();
