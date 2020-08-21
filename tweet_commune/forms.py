from django import forms

from tweet_commune.models.submission import Submission
from tweet_commune.twitter_settings import MAX_IMAGE_CHAR_COUNT


_EMPTY_SUBMISSION_MESSAGE = "Submission cannot be empty!"
_CAPTION_LENGTH_ERROR = "Image captions cannot be longer than {0} character!".format(MAX_IMAGE_CHAR_COUNT)


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
        if image and len(text) >= MAX_IMAGE_CHAR_COUNT:
            raise forms.ValidationError(
                _CAPTION_LENGTH_ERROR
            )
