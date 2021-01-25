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


    @staticmethod
    def get_action():
        raffle = Raffle(multiplier=5)
        while Submission.queue.length() > 0:
            submission = raffle.choices(Submission.queue.all())[0]
            action = SubmissionActions(submission)
            # Ensure Submission is valid
            if action.validate():
                return action
            else:
                # If invalid, flag
                action.flag()
        # Return None if queue is empty
        return None

    def handle(self, *args, **options):
        try:
            action = Command.get_action()
            if action:
                action.post()
            else:
                TweetLogger.empty_queue()
        except Exception as e:
            TweetLogger.critical(e)
