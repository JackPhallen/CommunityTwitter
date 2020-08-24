from django.db import models
from django.urls import reverse
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

from tweet_commune.twitter_settings import MAX_CHAR_COUNT


class SubmissionManager(models.Manager):
    """
    Custom model manager for Submission to interact with Submissions as a queue
    """

    def length(self, date=None):
        if not date:
            return self.get_queryset().count()
        else:
            # Get all Submissions created before date
            created = Submission.objects.all().filter(date_created__lte=date)
            # Get all Submissions posted before date
            posted = created.filter(date_sent__lte=date)
            return created.count() - posted.count()

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
    text = models.CharField(_("Text"), max_length=MAX_CHAR_COUNT, blank=True)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    sent = models.BooleanField(_("Was Posted"), default=False, editable=False)
    date_sent = models.DateTimeField(_("Date Posted"), editable=False, null=True)
    votes = models.IntegerField(_("Votes"), default=0, editable=False)
    image = models.ImageField(upload_to='image_submissions', blank=True)

    objects = models.Manager()
    queue = SubmissionManager()

    class Meta:
        verbose_name = _("Submission")
        verbose_name_plural = _("Submissions")

    def __unicode__(self):
        return smart_text(self.text)

    def get_absolute_url(self):  # new
        return reverse('submission_detail', args=[str(self.id)])
