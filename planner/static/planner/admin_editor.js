(function () {
    "use strict";

    function initAdminEditors() {
        if (typeof CodeMirror === "undefined") return;

        var textareas = document.querySelectorAll("textarea.admin-code-editor");
        if (!textareas.length) return;

        textareas.forEach(function (textarea) {
            if (textarea.dataset.cmReady === "true") return;

            var cm = CodeMirror.fromTextArea(textarea, {
                mode: "python",
                theme: "monokai",
                lineNumbers: true,
                indentUnit: 4,
                tabSize: 4,
                indentWithTabs: false,
                lineWrapping: true,
                autoCloseBrackets: true,
                matchBrackets: true,
                viewportMargin: Infinity,
                extraKeys: {
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

            /* Sync value back to textarea on change */
            cm.on("change", function () {
                textarea.value = cm.getValue();
            });

            textarea.dataset.cmReady = "true";
        });
    }

    /* Wait for DOM ready */
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initAdminEditors);
    } else {
        /* Small delay to ensure CodeMirror is loaded (scripts may be deferred) */
        setTimeout(initAdminEditors, 100);
    }
})();
