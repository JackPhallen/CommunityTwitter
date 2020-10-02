from django.contrib import admin
from django.contrib.auth import get_permission_codename

from tweet_commune.models.submission import Submission
from .forms import SubmissionModelForm


class SubmissionAdmin( admin.ModelAdmin ):
    form = SubmissionModelForm
    list_display = ('sent', 'flagged', 'text')
    list_filter = ('sent', 'flagged')
    actions = ['flag_submission', 'unflag_submission']

    def flag_submission(self, request, queryset):
        queryset.update(flagged=True)
    flag_submission.short_description = "Flag as inappropriate"
    flag_submission.allowed_permission = ('flag',)

    def unflag_submission(self, request, queryset):
        queryset.update(flagged=False)
    unflag_submission.short_description = "Unflag as inappropriate"
    unflag_submission.allowed_permission = ('unflag',)

    def has_flag_permission(self, request):
        """Does the user have the flag permission?"""
        opts = self.opts
        codename = get_permission_codename('flag', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    def has_unflag_permission(self, request):
        """Does the user have the unflag permission?"""
        opts = self.opts
        codename = get_permission_codename('unflag', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))


admin.site.register(Submission, SubmissionAdmin)
