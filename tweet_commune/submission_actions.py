from tweet_commune.tweet_blaster.email_config import EmailConfig
from tweet_commune.tweet_blaster.email_tweeter import EmailTweeter
from tweet_commune.tweet_blaster import _CONFIG_PATH, _PROFILE
from .logger.tweet_logger import TweetLogger


class SubmissionActions:
    """
    Invoke actions on Submission instances
    """

    def __init__(self, submission):
        self.submission = submission

    def post(self):
        """
        Posts a submission to Twitter
        """
        try:

            config = EmailConfig(_CONFIG_PATH, _PROFILE)
            tweeter = EmailTweeter(config)
            tweeter.send_tweet(self.submission.text)
            self.submission.sent = True
            self.submission.save()
            TweetLogger.success(self.submission.text)
        except Exception as e:
            TweetLogger.tweet_failed(e)
