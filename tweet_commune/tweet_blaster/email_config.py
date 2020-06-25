from configparser import ConfigParser


class EmailConfig:
    """
    Email configuration for Email Twitter
    """

    def __init__(self, config, profile):
        """
        :param config: path to email config file
        :param profile: profile of config file to use
        """
        parser = ConfigParser()
        parser.read(config)
        self.email = parser.get(profile, 'email')
        self.password = parser.get(profile, 'password')
        self.server = parser.get(profile, 'email-server')
        self.port = parser.get(profile, 'email-port')
        self.recipient = parser.get(profile, 'trigger-email')
        self.subject = parser.get(profile, 'trigger-subject')