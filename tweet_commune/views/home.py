from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from tweet_commune.models.submission import Submission
from ..forms import SubmissionModelForm


class HomeView(TemplateView):
    """
    Landing page view
    """

    template_name = "tweet_commune/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queue_length'] = Submission.queue.all().count()
        return context