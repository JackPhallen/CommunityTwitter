from django import forms

from tweet_commune.models.submission import Submission


class SubmissionModelForm(forms.ModelForm):
    """
    Custom form for Submission model
    """

    text = forms.CharField(widget=forms.Textarea, label=False)

    class Meta:
        model = Submission
        fields = '__all__'
