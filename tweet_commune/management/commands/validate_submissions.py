import datetime

from django.core.management.base import BaseCommand

from tweet_commune.submission_actions import SubmissionActions
from ...logger.tweet_logger import TweetLogger
from ...models.submission import Submission
from ...raffle import Raffle


class Command(BaseCommand):
    """
    Management command to validate all submissions in queue
    """

    help = "Validate all Submissions in queue"

    def add_arguments(self, parser):
        # Length (in days) of submissions to filter
        parser.add_argument(
            '--days',
            type=int,
            default=0,
            help='Filters all submissions created in the past n days.',
        )

    _ONE_DAY = datetime.timedelta(days=1)

    def handle(self, *args, **options):
        days = 1
        if options['days']:
            days = options['days']
        # 1 full day is the minimum allowed
        if days < 1:
            raise Exception("--days must be greater than 0")
        # Get all submissions created within the past n days
        from_date = datetime.date.today() - datetime.timedelta(days=options['days'])
        to_filter = Submission.objects.all().filter(date_created__gte=from_date)
        # Check each submission against the filter
        for submission in to_filter:
            action = SubmissionActions(submission)
            if not action.validate():
                action.flag()
