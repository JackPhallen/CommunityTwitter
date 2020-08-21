from django import forms

from tweet_commune.models.submission import Submission
from tweet_commune.twitter_settings import MAX_IMAGE_CHAR_COUNT, MAX_IMAGE_SIZE


_EMPTY_SUBMISSION_MESSAGE = "Submission cannot be empty!"
_CAPTION_LENGTH_ERROR = "Image captions cannot be longer than {0} character!".format(MAX_IMAGE_CHAR_COUNT)
_IMAGE_SIZE_ERROR = "Image is too big, must be less than {0} MB".format(
    MAX_IMAGE_SIZE / 1000000
)


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

        if image:
            # Ensure text accompanying an image is not too long
            if len(text) >= MAX_IMAGE_CHAR_COUNT:
                raise forms.ValidationError(
                    _CAPTION_LENGTH_ERROR
                )
            # Ensure image does not exceed max allowed size
            if image.size >= MAX_IMAGE_SIZE:
                raise forms.ValidationError(
                    _IMAGE_SIZE_ERROR
                )

