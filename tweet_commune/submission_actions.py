import datetime
import pytz

from tweet_commune.tweet_blaster import _CONFIG_PATH, _PROFILE, _IMG_PROFILE
from tweet_commune.tweet_blaster.email_config import EmailConfig
from tweet_commune.tweet_blaster.email_tweeter import EmailTweeter
from .logger.tweet_logger import TweetLogger


class SubmissionActions:
    """
    Invoke actions on Submission instances
    """

    TZ = pytz.timezone('US/Eastern')

    def __init__(self, submission):
        self.submission = submission

    def post(self):
        """
        Posts a submission to Twitter
        """
        try:
            if self.submission.image:
                config = EmailConfig(_CONFIG_PATH, _IMG_PROFILE)
                tweeter = EmailTweeter(config)
                tweeter.send_tweet(self.submission.text, img_path=self.submission.image.path)
            else:
                config = EmailConfig(_CONFIG_PATH, _PROFILE)
                tweeter = EmailTweeter(config)
                tweeter.send_tweet(self.submission.text)
            self.submission.sent = True
            self.submission.date_sent = SubmissionActions.TZ.localize(datetime.datetime.now())
            self.submission.save()
            TweetLogger.success(self.submission.text)
        except Exception as e:
            TweetLogger.tweet_failed(e)
