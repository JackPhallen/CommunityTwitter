from .model_logger import ModelLogger
from ..models.log_entry import LogEntry


class TweetLogger:
    """
    Logger for send_tweet actions
    """

    _EMPTY_QUEUE_MESSAGE = 'The submission queue is empty!'
    _TWEET_SENT_MESSAGE = 'Successfully tweeted: "{0}"'
    _ERROR_MESSAGE = 'Failed to send tweet! ERROR: "{0}"'
    _CRITICAL_MESSAGE = 'CRITICAL ERROR: "{0}"'

    # Create model logger for LogEntry model
    _logger = ModelLogger(LogEntry)

    @staticmethod
    def empty_queue():
        """
        Log empty queue status
        """
        TweetLogger._logger.warn(TweetLogger._EMPTY_QUEUE_MESSAGE)

    @staticmethod
    def success(text):
        """
        Log successful posting of tweet
        :param text: content of tweet
        """
        message = TweetLogger._TWEET_SENT_MESSAGE.format(text)
        TweetLogger._logger.info(message)

    @staticmethod
    def tweet_failed(error):
        """
        Log error when posting tweet
        :param error: Exception that occurred
        """
        message = TweetLogger._ERROR_MESSAGE.format(str(error))
        TweetLogger._logger.error(message)

    @staticmethod
    def critical(error):
        """
        Log any error not caught
        :param error: Exception that occurred
        """
        message = TweetLogger._CRITICAL_MESSAGE.format(str(error))
        TweetLogger._logger.error(message)
