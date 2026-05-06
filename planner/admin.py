from django.contrib import admin
from django.db.models import Count, Q
from django.template.defaultfilters import truncatechars
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Submission, Task


# ── Custom admin widgets ─────────────────────────────────────

class CodeEditorWidget(admin.widgets.AdminTextareaWidget):
    """Textarea with a CSS class for CodeMirror initialization."""

    def __init__(self, attrs=None):
        defaults = {"class": "admin-code-editor", "rows": 14}
        if attrs:
            defaults.update(attrs)
        super().__init__(attrs=defaults)


class AdminCodeForm(admin.options.forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "starter_code": CodeEditorWidget(),
            "tests": CodeEditorWidget(attrs={"rows": 16}),
            "description": admin.widgets.AdminTextareaWidget(attrs={"rows": 6}),
        }


# ── Task Admin ───────────────────────────────────────────────

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = AdminCodeForm

    # ── List view ──
    list_display = (
        "task_label",
        "title",
        "style_badge",
        "has_starter",
        "test_count_display",
        "submissions_stat",
        "created_at",
        "complexity",
    )
    list_filter = ("complexity", "style")
    search_fields = ("title", "description")
    list_per_page = 25
    list_editable = ()
    ordering = ("order",)

    # ── Form layout ──
    fieldsets = (
        ("📋 Основное", {
            "fields": ("title", "description", "style", "complexity"),
            "description": "Название и описание задачи, которые видит ученик.",
        }),
        ("📁 Расположение", {
            "fields": ("order",),
            "description": "Порядок вывода задачи.",
        }),
        ("💻 Шаблон кода", {
            "fields": ("starter_code",),
            "description": (
                "Начальный код, который увидит ученик при открытии задачи. "
                "Обычно содержит <code>def function_name(...):</code> или <code>class ClassName:</code> "
                "с <code>pass</code> вместо реализации."
            ),
        }),
        ("✅ Тесты", {
            "fields": ("tests",),
            "description": (
                "Набор <code>assert</code>-выражений для автопроверки. Пример:<br>"
                "<code>assert sum_even([1, 2, 3, 4]) == 6</code><br>"
                "<code>assert sum_even([]) == 0</code><br><br>"
                "Поддерживаются формы: <code>assert expr == value</code> и <code>assert expr is True/False/None</code>"
            ),
        }),
    )

    # ── Actions ──
    actions = ["duplicate_tasks"]

    @admin.action(description="📋 Дублировать выбранные задачи")
    def duplicate_tasks(self, request, queryset):
        count = 0
        for task in queryset:
            # Find next available order
            max_order = (
                Task.objects.order_by("-order")
                .values_list("order", flat=True)
                .first()
            ) or 0
            Task.objects.create(
                order=max_order + 1,
                title=f"{task.title} (копия)",
                description=task.description,
                style=task.style,
                complexity=task.complexity,
                starter_code=task.starter_code,
                tests=task.tests,
            )
            count += 1
        self.message_user(request, f"Продублировано задач: {count}")

    # ── Custom columns ──
    @admin.display(description="Задача", ordering="order")
    def task_label(self, obj):
        return format_html(
            '<span style="font-family: monospace; font-weight: 600; '
            'color: #7c5cfc; font-size: 13px;">#{}</span>',
            obj.order,
        )

    @admin.display(description="Стиль")
    def style_badge(self, obj):
        colors = {
            "procedural": ("#60a5fa", "#1e3a5f"),
            "functional": ("#fb923c", "#5f3415"),
            "oop": ("#a78bfa", "#3b2d6b"),
        }
        fg, bg = colors.get(obj.style, ("#aaa", "#333"))
        return format_html(
            '<span style="background: {}; color: {}; padding: 3px 10px; '
            'border-radius: 12px; font-size: 11px; font-weight: 600;">{}</span>',
            bg, fg, obj.get_style_display(),
        )

    @admin.display(description="Шаблон", boolean=True)
    def has_starter(self, obj):
        return bool(obj.starter_code.strip())

    @admin.display(description="Тестов")
    def test_count_display(self, obj):
        count = sum(
            1 for line in obj.tests.splitlines()
            if line.strip().startswith("assert ")
        )
        return format_html(
            '<span style="font-family: monospace; font-weight: 500;">{}</span>',
            count,
        )

    @admin.display(description="Решений")
    def submissions_stat(self, obj):
        total = obj._sub_total if hasattr(obj, "_sub_total") else 0
        passed = obj._sub_passed if hasattr(obj, "_sub_passed") else 0
        if total == 0:
            return mark_safe('<span style="color: #888;">—</span>')
        return format_html(
            '<span style="color: {}; font-weight: 500;">{}/{}</span>',
            "#34d399" if passed > 0 else "#f87171",
            passed,
            total,
        )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(
            _sub_total=Count("submission"),
            _sub_passed=Count("submission", filter=Q(submission__passed=True)),
        )
        return qs

    # ── Auto-fill order for new tasks ──
    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        last_task = Task.objects.order_by("-order").first()
        if last_task:
            initial.setdefault("order", last_task.order + 1)
        else:
            initial.setdefault("order", 1)
        return initial

    class Media:
        css = {
            "all": (
                "https://cdn.jsdelivr.net/npm/codemirror@5.65.16/lib/codemirror.css",
                "https://cdn.jsdelivr.net/npm/codemirror@5.65.16/theme/monokai.css",
                "planner/admin_custom.css",
            )
        }
        js = (
            "https://cdn.jsdelivr.net/npm/codemirror@5.65.16/lib/codemirror.js",
            "https://cdn.jsdelivr.net/npm/codemirror@5.65.16/mode/python/python.js",
            "https://cdn.jsdelivr.net/npm/codemirror@5.65.16/addon/edit/closebrackets.js",
            "https://cdn.jsdelivr.net/npm/codemirror@5.65.16/addon/edit/matchbrackets.js",
            "planner/admin_editor.js",
        )


# ── Submission Admin ─────────────────────────────────────────

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "task",
        "status_badge",
        "created_at",
    )
    list_filter = ("user", "passed", "created_at", "task__complexity", "task__style")
    search_fields = ("user__username", "task__title")
    list_per_page = 30
    readonly_fields = ("user", "task", "code", "passed", "output", "error", "created_at")
    ordering = ("-created_at",)

    fieldsets = (
        ("Информация", {
            "fields": ("user", "task", "passed", "created_at"),
        }),
        ("Код ученика", {
            "fields": ("code",),
            "classes": ("collapse",),
        }),
        ("Результат", {
            "fields": ("output", "error"),
            "classes": ("collapse",),
        }),
    )

    def has_add_permission(self, request):
        return False

    @admin.display(description="Статус")
    def status_badge(self, obj):
        if obj.passed:
            return mark_safe(
                '<span style="background: rgba(52,211,153,0.15); color: #34d399; '
                'padding: 3px 10px; border-radius: 12px; font-size: 11px; '
                'font-weight: 700;">✓ OK</span>'
            )
        return mark_safe(
            '<span style="background: rgba(248,113,113,0.15); color: #f87171; '
            'padding: 3px 10px; border-radius: 12px; font-size: 11px; '
            'font-weight: 700;">✕ FAIL</span>'
        )

    @admin.display(description="Код")
    def code_preview(self, obj):
        preview = truncatechars(obj.code.replace("\n", " ↵ "), 80)
        return format_html(
            '<span style="font-family: monospace; font-size: 11px; color: #999;">{}</span>',
            preview,
        )


# ── Admin site customization ─────────────────────────────────
admin.site.site_header = "Python Problemset — Админ-панель"
admin.site.site_title = "Problemset Admin"
admin.site.index_title = "Управление задачами"
