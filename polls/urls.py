from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("polls", views.submit_polls, name="submit-poll"),
    path("polls/<int:pk>/", views.delete_polls, name="delete-poll"),
]
