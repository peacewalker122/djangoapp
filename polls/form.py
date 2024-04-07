from polls.models import Polls
from django import forms


class PollsForm(forms.ModelForm):
    class Meta:
        model = Polls
        fields = (
            "title",
            "body",
        )
