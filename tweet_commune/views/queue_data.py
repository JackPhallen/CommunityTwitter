from django.views.generic import TemplateView

from tweet_commune.queue_history import QueueHistory


class QueueDataView(TemplateView):
    """
    Landing page view
    """

    template_name = "tweet_commune/queue_data.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queue_history = QueueHistory()
        data = queue_history.json
        context['queue_history'] = queue_history.json
        return context
