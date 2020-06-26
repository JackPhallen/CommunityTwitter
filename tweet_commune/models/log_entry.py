from django.db import models
from django.utils.translation import ugettext_lazy as _

_LEVELS = {
    (1, "INFO"),
    (2, "WARN"),
    (3, "ERROR")
}


class LogManager(models.Manager):

    def top(self, count=1):
        """
        Retrieve the submission at the top of the queue
        """
        return self.all()[:count]

    def is_up(self):
        """
        Check if last log entry was an error

        :return: True if no error
        """
        entry = self.all().first()
        if entry:
            return not entry.is_error()
        else:
            # If no LogEntries, assume site is working
            return True


class LogEntry(models.Model):
    """
    Model representing log entry from tweet posting tasks
    """

    message = models.TextField(_("Message"))
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)
    level = models.IntegerField(_("Level"), choices=_LEVELS, blank=True, null=True)

    objects = models.Manager()
    LogManager = LogManager()

    class Meta:
        verbose_name = _("Log Entry")
        verbose_name_plural = _("Log Entries")
        ordering = ['-timestamp']

    def is_error(self):
        """
        Determine if log entry represents an error
        :return:
        """
        return self.level == 3

    def row_class(self):
        if self.level == 1:
            return "table-info"
        elif self.level == 2:
            return "table-warning"
        elif self.level == 3:
            return "table-danger"
        else:
            return "table-light"
