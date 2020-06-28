import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


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

    def _format(self, body, img_path=None):
        """
        Format email

        :param body: Body of the email
        :param img_path: path to image attachment
        """
        msg = MIMEMultipart()
        msg['Subject'] = self._config.subject

        msg['From'] = self._config.email
        msg['To'] = self._config.recipient

        msg.attach(MIMEText(body))

        # if image provided, attach
        if img_path:
            with open(img_path, 'rb') as img:
                mime_img = MIMEImage(img.read())
                msg.attach(mime_img)

        return msg.as_string()

    def send_tweet(self, tweet, img_path=None):
        """
        Send email to trigger tweet

        :param tweet: content of the tweet
        :param img_path: path to image attachment
        """
        email_content = self._format(tweet, img_path)
        connection = self._get_connection()
        connection.sendmail(self._config.email, self._config.recipient, email_content)
        connection.quit()
