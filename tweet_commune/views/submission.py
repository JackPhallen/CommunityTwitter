from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from tweet_commune.models.submission import Submission
from ..forms import SubmissionModelForm


class SubmissionCreateView(SuccessMessageMixin, CreateView):
    """
    CreateView for Submission model
    """
    model = Submission
    form_class = SubmissionModelForm
    success_url = reverse_lazy("submission_list")
    success_message = 'Success!'
