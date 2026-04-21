from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
import re

from .forms import SubmissionForm
from .models import Submission, Task
from .utils import run_tests

DAY_NAMES = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье",
}

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
    tasks_by_day = {day: list(Task.objects.filter(day_index=day)) for day in range(1, 8)}
    passed_task_ids = set()
    if request.user.is_authenticated:
        passed_task_ids = set(
            Submission.objects.filter(user=request.user, passed=True).values_list("task_id", flat=True)
        )

    days = []
    for day in range(1, 8):
        day_tasks = tasks_by_day.get(day, [])
        completed = sum(1 for task in day_tasks if task.id in passed_task_ids)
        total = len(day_tasks)
        percent = int((completed / total) * 100) if total else 0
        days.append(
            {
                "index": day,
                "name": DAY_NAMES[day],
                "tasks": day_tasks,
                "completed": completed,
                "total": total,
                "percent": percent,
            }
        )

    return render(request, "planner/dashboard.html", {"days": days})


def day_view(request, day: int):
    if day not in DAY_NAMES:
        return redirect("dashboard")

    tasks = list(Task.objects.filter(day_index=day))
    passed_task_ids = set()
    if request.user.is_authenticated:
        passed_task_ids = set(
            Submission.objects.filter(user=request.user, passed=True).values_list("task_id", flat=True)
        )

    return render(
        request,
        "planner/day.html",
        {
            "day": day,
            "day_name": DAY_NAMES[day],
            "tasks": tasks,
            "passed_task_ids": passed_task_ids,
        },
    )


@login_required
def task_detail(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    last_submission = Submission.objects.filter(user=request.user, task=task).first()
    next_task = (
        Task.objects.filter(
            Q(day_index=task.day_index, order__gt=task.order) | Q(day_index__gt=task.day_index)
        )
        .order_by("day_index", "order")
        .first()
    )

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
