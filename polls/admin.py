from django.contrib import admin
from polls.models import Polls, PollsQuestion


# Register your models here.

admin.site.register(Polls)
admin.site.register(PollsQuestion)
