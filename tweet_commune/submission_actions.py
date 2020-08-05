import datetime
import pytz

from .twitter_api import TwitterAPI
from .twitter_settings import *
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
            api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
            if self.submission.image:
                api.post(self.submission.text, img_paths=[self.submission.image.path, ])
            else:
                api.post(self.submission.text)
            self.submission.sent = True
            self.submission.date_sent = SubmissionActions.TZ.localize(datetime.datetime.now())
            self.submission.save()
            TweetLogger.success(self.submission.text)
        except Exception as e:
            TweetLogger.tweet_failed(e)
