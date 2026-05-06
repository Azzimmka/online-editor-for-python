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


    title = models.CharField(max_length=200)
    description = models.TextField()
    style = models.CharField(max_length=20, choices=STYLE_CHOICES)
    starter_code = models.TextField(blank=True)
    tests = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    complexity = models.CharField(max_length=20, choices=COMPLEXITY_CHOICES, default=COMPLEXITY_MEDIUM)

    class Meta:
        ordering = ["complexity", "id"]
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self) -> str:
        return self.title


class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Ученик")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Задача")
    code = models.TextField(verbose_name="Код")
    passed = models.BooleanField(default=False, verbose_name="Пройдено")
    output = models.TextField(blank=True, verbose_name="Вывод")
    error = models.TextField(blank=True, verbose_name="Ошибка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Решение"
        verbose_name_plural = "Решения учеников"

    def __str__(self) -> str:
        status = "OK" if self.passed else "FAIL"
        return f"{self.user} - {self.task} ({status})"
