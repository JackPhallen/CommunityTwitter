from django import forms

from tweet_commune.models.submission import Submission


_MAX_CAPTION_LENGTH = 217
_EMPTY_SUBMISSION_MESSAGE = "Submission cannot be empty!"
_CAPTION_LENGTH_ERROR = "Image captions cannot be longer than {0} character!".format(_MAX_CAPTION_LENGTH)


class SubmissionModelForm(forms.ModelForm):
    """
    Custom form for Submission model
    """

    text = forms.CharField(widget=forms.Textarea, label=False, required=False)

    class Meta:
        model = Submission
        fields = '__all__'

    def clean(self):
        """
        Ensure Submission includes either an image or text content and meets length requirements
        """
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        text = cleaned_data.get("text")

        # Ensure Submission includes either text or an image
        if not image and not text:
            raise forms.ValidationError(
                _EMPTY_SUBMISSION_MESSAGE
            )

        # Ensure text accompanying an image is not too long
        if image and len(text) >= _MAX_CAPTION_LENGTH:
            raise forms.ValidationError(
                _CAPTION_LENGTH_ERROR
            )
