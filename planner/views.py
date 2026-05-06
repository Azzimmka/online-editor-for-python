from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
import re

from .forms import SubmissionForm
from .models import Submission, Task
from .utils import run_tests

def _extract_examples(test_code: str, limit: int = 4) -> list[str]:
    examples = []
    for raw_line in test_code.splitlines():
        line = raw_line.strip()
        if not line.startswith("assert "):
            continue

        match = re.match(r"assert\s+(.+?)\s+==\s+(.+)$", line)
        if match:
            expr, expected = match.groups()
            examples.append(f"{expr} -> {expected}")
            continue

        match = re.match(r"assert\s+(.+?)\s+is\s+(True|False|None)\s*$", line)
        if match:
            expr, expected = match.groups()
            examples.append(f"{expr} -> {expected}")
            continue

        if len(examples) >= limit:
            break

    return examples[:limit]


def dashboard(request):
    all_tasks = list(Task.objects.all().order_by("complexity", "id"))
    passed_task_ids = set()
    if request.user.is_authenticated:
        passed_task_ids = set(
            Submission.objects.filter(user=request.user, passed=True).values_list("task_id", flat=True)
        )

    selected_style = request.GET.get("style", "all")
    available_styles = {choice for choice, _ in Task.STYLE_CHOICES}
    if selected_style not in available_styles:
        selected_style = "all"

    selected_complexity = request.GET.get("complexity", "all")
    available_complexities = {choice for choice, _ in Task.COMPLEXITY_CHOICES}
    if selected_complexity not in available_complexities and selected_complexity != "all":
        selected_complexity = "all"

    tasks = all_tasks
    if selected_style != "all":
        tasks = [task for task in tasks if task.style == selected_style]
    if selected_complexity != "all":
        tasks = [task for task in tasks if task.complexity == selected_complexity]

    style_filters = [
        {
            "value": "all",
            "label": "Все стили",
            "count": len(all_tasks),
            "active": selected_style == "all",
        }
    ]
    for value, label in Task.STYLE_CHOICES:
        style_filters.append(
            {
                "value": value,
                "label": label,
                "count": sum(1 for task in all_tasks if task.style == value),
                "active": selected_style == value,
            }
        )

    complexity_filters = [
        {
            "value": "all",
            "label": "Все сложности",
            "active": selected_complexity == "all",
        }
    ]
    for value, label in Task.COMPLEXITY_CHOICES:
        complexity_filters.append(
            {
                "value": value,
                "label": label,
                "active": selected_complexity == value,
            }
        )

    solved_total = len(passed_task_ids)
    total_tasks = len(all_tasks)
    unsolved_total = max(total_tasks - solved_total, 0)
    solved_percent = int((solved_total / total_tasks) * 100) if total_tasks else 0
    filtered_total = len(tasks)

    style_stats = []
    for style_value, style_label in Task.STYLE_CHOICES:
        style_tasks = [task for task in all_tasks if task.style == style_value]
        style_total = len(style_tasks)
        style_solved = sum(1 for task in style_tasks if task.id in passed_task_ids)
        style_percent = int((style_solved / style_total) * 100) if style_total else 0
        style_stats.append(
            {
                "value": style_value,
                "label": style_label,
                "total": style_total,
                "solved": style_solved,
                "percent": style_percent,
            }
        )

    return render(
        request,
        "planner/dashboard.html",
        {
            "tasks": tasks,
            "passed_task_ids": passed_task_ids,
            "style_filters": style_filters,
            "complexity_filters": complexity_filters,
            "solved_total": solved_total,
            "total_tasks": total_tasks,
            "unsolved_total": unsolved_total,
            "solved_percent": solved_percent,
            "filtered_total": filtered_total,
            "style_stats": style_stats,
            "selected_style": selected_style,
            "selected_complexity": selected_complexity,
        },
    )


def day_view(request, day: int):
    # Backward compatibility redirect
    return redirect("dashboard")


@login_required
def task_detail(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    last_submission = Submission.objects.filter(user=request.user, task=task).first()
    next_task = Task.objects.filter(id__gt=task.id).order_by("id").first()

    initial_code = task.starter_code
    if last_submission:
        initial_code = last_submission.code

    result = None
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        form.fields["code"].widget.attrs["data-task-id"] = str(task.id)
        if form.is_valid():
            code = form.cleaned_data["code"]
            result = run_tests(code, task.tests)
            Submission.objects.create(
                user=request.user,
                task=task,
                code=code,
                passed=result["passed"],
                output=result["output"],
                error=result["error"],
            )
    else:
        form = SubmissionForm(initial={"code": initial_code})
        form.fields["code"].widget.attrs["data-task-id"] = str(task.id)

    examples = _extract_examples(task.tests)
    passed = False
    if result is not None:
        passed = result["passed"]
    elif last_submission:
        passed = last_submission.passed

    back_url = f"{reverse('dashboard')}?complexity={task.complexity}"

    return render(
        request,
        "planner/task_detail.html",
        {
            "task": task,
            "form": form,
            "result": result,
            "last_submission": last_submission,
            "examples": examples,
            "next_task": next_task,
            "passed": passed,
            "back_url": back_url,
        },
    )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})
