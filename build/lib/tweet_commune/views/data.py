from django.views.generic import TemplateView

from tweet_commune.calc.queue_history import QueueHistory
from tweet_commune.calc.submission_history import SubmissionHistory


class DataView(TemplateView):
    """
    Landing page view
    """

    template_name = "tweet_commune/data.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queue_history = QueueHistory()
        submission_data = SubmissionHistory()
        context['queue_history'] = queue_history.json
        context['submission_data'] = submission_data.json
        return context
