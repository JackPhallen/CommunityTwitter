class ModelLogger:
    """
    Generic logger for log model
    """

    def __init__(self, model):
        self.model = model

    def _log(self, level, message):
        self.model(level=level, message=message).save()

    def info(self, message):
        self._log(1, message)

    def warn(self, message):
        self._log(2, message)

    def error(self, message):
        self._log(3, message)