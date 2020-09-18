import datetime
import json

from django.core.serializers.json import DjangoJSONEncoder

from tweet_commune.models.submission import Submission


class SubmissionHistory:

    _ONE_DAY = datetime.timedelta(days=1)

    def __init__(self):
        self.data = SubmissionHistory._build()

    @staticmethod
    def _build():
        today = datetime.date.today()
        date = Submission.objects.earliest('date_created').date_created.date()
        history = []
        while date <= today:
            submissions = Submission.objects.all().filter(date_created__date=date)
            count = submissions.count()
            history.append([
                date,
                count
            ])
            date += SubmissionHistory._ONE_DAY
        return history

    @property
    def json(self):
        return json.dumps(self.data, cls=DjangoJSONEncoder)
