import logging
import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from polls.models import Polls
from django.core import serializers
from polls.form import PollsForm
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse

logger = logging.getLogger("logger")


@login_required
def index(request):
    cur_user = request.user

    polls = Polls.objects.raw(
        """
SELECT
    pp.*,
    json_agg(p) as questions
FROM polls_polls pp
LEFT JOIN public.polls_pollsquestion p on pp.id = p.poll_id
WHERE pp.created_by_id = %s AND pp.deleted_at IS NULL
GROUP BY pp.id, title, body, created_at, updated_at, deleted_at, created_by_id
""",
        [cur_user.id],
    )

    logger.info("incoming request", extra={"request": request, "user": cur_user})
    for i, poll in enumerate(polls):
        for question in poll.questions:
            questions = serializers.deserialize("json", question)
            question = questions
        poll.modal_id = f"detailModal{i}"

    context = {"polls": polls, "form": PollsForm()}

    return render(request, "index.html", context)


@login_required
@require_POST
def submit_polls(request):
    logger.info("incoming request", extra={"request": request})
    form = PollsForm(request.POST)
    try:
        if form.is_valid():
            poll = form.save(commit=False)
            poll.created_by = request.user
            poll.save()

            context = {"poll": poll}
            return render(request, "index.html#polls-partial", context)
        else:
            return HttpResponse("form is not valid", status=400)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)


@login_required
@require_http_methods(["DELETE"])
def delete_polls(request, pk=None):
    logger.info("incoming request", extra={"request": request, "pk": pk})

    try:

        poll = get_object_or_404(Polls, pk=pk, created_by=request.user)
        poll.deleted_at = datetime.datetime.now()
        poll.save()
        context = {"poll": poll}

        return render(request, "index.html#polls-partial", context)
    except Exception as e:
        logger.error(f"Error: {str(e)}", extra={"request": request, "pk": pk})
        return HttpResponse(f"Error: {str(e)}", status=500)
