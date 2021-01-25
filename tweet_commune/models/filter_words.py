from django.db import models
from django.utils.translation import ugettext_lazy as _


class FilterWordManager(models.Manager):

    def get_enabled(self):
        """
        Retrieve all filter words currently enabled
        """
        return self.all().filter(enabled=True)

    def contains(self, text):
        """
        If text includes filtered words, return true
        """
        for entry in self.get_enabled():
            if entry.contains(text):
                return True
        return False


class FilterWord(models.Model):
    """
    Each comma delimited entry represents words that are banned when used together
    """

    words = models.TextField(_("Words"))
    enabled = models.BooleanField(_("Enabled"), default=True)

    objects = models.Manager()
    FilterWordManager = FilterWordManager()

    class Meta:
        verbose_name = _("Filter Word")
        verbose_name_plural = _("Filter Words")

    def contains(self, text):
        """
        If text includes ALL filtered words, return true

        example: if words field is 'tweet,commune', will return True IFF text contains
        substring 'tweet' AND substring 'commune'
        """
        words = self.words.split(",")
        for word in words:
            if word.lower() not in text.lower():
                return False
        return True
