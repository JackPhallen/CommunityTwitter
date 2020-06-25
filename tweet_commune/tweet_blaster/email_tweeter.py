import smtplib


class EmailTweeter:
    """
    Post tweets via emaill
    """

    def __init__(self, config):
        """
        :type config: EmailConfig
        :param config: Email config to send tweets
        """
        self._config = config

    def _get_connection(self):
        """
        Create connection to smtp server

        :return: SMTP connection
        """
        connection = smtplib.SMTP(self._config.server, self._config.port)
        connection.starttls()
        connection.login(self._config.email, self._config.password)
        return connection

    def _format(self, body):
        """
        Format email
        :param body: Body of the email
        :return:
        """
        return "Subject: {0}\n\n{1}".format(self._config.subject, body)

    def send_tweet(self, tweet):
        """
        Send email to trigger tweet
        :param tweet: content of the tweet
        """
        email_content = self._format(tweet)
        connection = self._get_connection()
        connection.sendmail(self._config.email, self._config.recipient, email_content)
        connection.quit()