from django.db import models
from django.urls import reverse
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _


class SubmissionManager(models.Manager):
    """
    Custom model manager for Submission to interact with Submissions as a queue
    """

    def get_queryset(self):
        """
        Override get_queryset to return Submissions not yet posted ordered by date
        :return:
        """
        return super().get_queryset().filter(sent=False).order_by('date_created')

    def top(self):
        """
        Retrieve the submission at the top of the queue

        :return:
        """
        return self.all().first()


class Submission(models.Model):
    text = models.CharField(_("Text"), max_length=240)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    sent = models.BooleanField(_("Was Posted"), default=False, editable=False)
    votes = models.IntegerField(_("Votes"), default=0, editable=False)

    objects = models.Manager()
    queue = SubmissionManager()

    class Meta:
        verbose_name = _("Submission")
        verbose_name_plural = _("Submissions")


    def __unicode__(self):
        return smart_text(self.text)

    def get_absolute_url(self):  # new
        return reverse('submission_detail', args=[str(self.id)])
