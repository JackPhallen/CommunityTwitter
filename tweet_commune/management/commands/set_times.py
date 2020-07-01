import datetime
import pytz

from django.core.management.base import BaseCommand

from tweet_commune.models.submission import Submission


class Command(BaseCommand):
    """
    Management command to retroactively set Submission sent times
    """

    help = "Retroactively set Submission sent time"

    START_TIME = datetime.time(hour=10)
    END_TIME = datetime.time(hour=21, minute=30)
    POST_FREQ_MINS = 30
    TZ = pytz.timezone('US/Eastern')

    def handle(self, *args, **options):
        """
        For each posted tweet, retroactively set the datetime it was posted
        """
        timestamp = Command.now_rounded()
        queryset = Submission.objects.all().filter(sent=True).order_by('-date_created')
        for submission in queryset:
            localized_dt = Command.TZ.localize(timestamp)
            submission.date_sent = localized_dt
            submission.save()
            timestamp = Command.get_next_time(timestamp)

    @staticmethod
    def get_next_time(current):
        """
        Get the next time a tweet was posted before current
        :param current: Time a tweet was posted
        :return: datetime representing the previous tweet time
        """
        next_datetime = current - datetime.timedelta(minutes=30)
        if next_datetime.time() < Command.START_TIME:
            next_day = next_datetime - datetime.timedelta(days=1)
            next_datetime = datetime.datetime.combine(next_day, Command.END_TIME)
        return next_datetime

    @staticmethod
    def now_rounded():
        """
        Rounds down to nearest 30 minutes
        """
        now = datetime.datetime.now()
        return now - datetime.timedelta(minutes=now.minute % Command.POST_FREQ_MINS,
                                        seconds=now.second,
                                        microseconds=now.microsecond)

