from django.views.generic import TemplateView
from django.core.serializers.json import DjangoJSONEncoder

import json
from tweet_commune.models.log_entry import LogEntry
from tweet_commune.models.submission import Submission


class HomeView(TemplateView):
    """
    Landing page view
    """

    template_name = "tweet_commune/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queue_length'] = Submission.queue.length()
        log_times = LogEntry.LogManager.top()
        context['last_log'] = json.dumps(log_times[0].timestamp, cls=DjangoJSONEncoder)
        context['is_up'] = LogEntry.LogManager.is_up()
        return context
