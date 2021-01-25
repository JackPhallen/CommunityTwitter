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

    def handle(self, *args, **options):
        for submission in Submission.queue.all():
            action = SubmissionActions(submission)
            if not action.validate():
                action.flag()
