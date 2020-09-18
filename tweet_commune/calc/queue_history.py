import datetime
import json

from django.core.serializers.json import DjangoJSONEncoder

from tweet_commune.models.submission import Submission


class QueueHistory:

    _ONE_DAY = datetime.timedelta(days=1)

    def __init__(self):
        self.data = QueueHistory._build()

    @staticmethod
    def _build():
        today = datetime.date.today()
        date = Submission.objects.earliest('date_created').date_created.date()
        history = []
        while date <= today:
            length = Submission.queue.length(date=date)
            history.append([
                date,
                length
            ])
            date += QueueHistory._ONE_DAY
        return history

    @property
    def json(self):
        return json.dumps(self.data, cls=DjangoJSONEncoder)
