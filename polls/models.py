from core import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):
    pass


class Polls(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # this column below doesn't exist in the db
    modal_id = ""

    def __str__(self):
        return self.title


class PollsQuestion(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now=True)
    MULTIPLE_CHOICE = "MC"
    SINGLE_CHOICE = "SC"
    TEXT = "TX"
    QUESTION_TYPE_CHOICES = [
        (MULTIPLE_CHOICE, "Multiple Choice"),
        (SINGLE_CHOICE, "Single Choice"),
        (TEXT, "Text"),
    ]
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE_CHOICES)

    def __str__(self):
        return self.question_text


class Responses(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    last_opened_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.poll.title
