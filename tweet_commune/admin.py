from django.contrib import admin
from tweet_commune.models.submission import Submission
from .forms import SubmissionModelForm


class SubmissionAdmin( admin.ModelAdmin ):
    form = SubmissionModelForm


admin.site.register(Submission, SubmissionAdmin)
