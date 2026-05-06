from django.conf import settings
from django.db import models




class Task(models.Model):
    STYLE_PROCEDURAL = "procedural"
    STYLE_FUNCTIONAL = "functional"
    STYLE_OOP = "oop"

    COMPLEXITY_EASY = "easy"
    COMPLEXITY_MEDIUM = "medium"
    COMPLEXITY_HARD = "hard"

    # Список вариантов: (значение в базе, отображаемое имя)
    COMPLEXITY_CHOICES = [
        (COMPLEXITY_EASY, "Легко"),
        (COMPLEXITY_MEDIUM, "Средне"),
        (COMPLEXITY_HARD, "Сложно"),
    ]

    STYLE_CHOICES = [
        (STYLE_PROCEDURAL, "Процедурный"),
        (STYLE_FUNCTIONAL, "Функциональный"),
        (STYLE_OOP, "ООП"),
    ]

    day_index = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    style = models.CharField(max_length=20, choices=STYLE_CHOICES)
    starter_code = models.TextField(blank=True)
    tests = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    complexity = models.CharField(max_length=20, choices=COMPLEXITY_CHOICES, default=COMPLEXITY_MEDIUM)

    class Meta:
        unique_together = ("day_index", "order")
        ordering = ["day_index", "order"]

    def __str__(self) -> str:
        return f"Day {self.day_index} #{self.order}: {self.title}"


class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    code = models.TextField()
    passed = models.BooleanField(default=False)
    output = models.TextField(blank=True)
    error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        status = "OK" if self.passed else "FAIL"
        return f"{self.user} - {self.task} ({status})"
