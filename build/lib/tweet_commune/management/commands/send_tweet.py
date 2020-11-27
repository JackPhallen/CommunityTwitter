from django.core.management.base import BaseCommand

from tweet_commune.submission_actions import SubmissionActions
from ...logger.tweet_logger import TweetLogger
from ...models.submission import Submission
from ...raffle import Raffle


class Command(BaseCommand):
    """
    Management command to post Submission to Twitter
    """

    help = "Post the top submission"

    def handle(self, *args, **options):
        try:
            raffle = Raffle(multiplier=5)
            submission = raffle.choices(Submission.queue.all())[0]
            if submission:
                actions = SubmissionActions(submission)
                actions.post()
            else:
                TweetLogger.empty_queue()
        except Exception as e:
            TweetLogger.critical(e)
