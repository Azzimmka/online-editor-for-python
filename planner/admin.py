from django.contrib import admin

from .models import Submission, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("day_index", "order", "title", "style")
    list_filter = ("day_index", "style")
    search_fields = ("title", "description")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("user", "task", "passed", "created_at")
    list_filter = ("passed", "created_at")
    search_fields = ("user__username", "task__title")
