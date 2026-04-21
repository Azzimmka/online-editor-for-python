from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("day/<int:day>/", views.day_view, name="day"),
    path("task/<int:task_id>/", views.task_detail, name="task_detail"),
    path("register/", views.register, name="register"),
]
