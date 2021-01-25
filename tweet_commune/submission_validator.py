from .models.filter_words import FilterWord


class SubmissionValidator:
    """
    Validates submission
    TODO: include validator for file type, file size and text length constraints
    """

    def validate(self, submission):
        """
        Returns true if Submission meets constraints
        """
        if not self.validate_filter(submission.text):
            return False
        return True

    def validate_filter(self, text):
        """
        Validate that Submission passes filter
        """
        return not FilterWord.FilterWordManager.contains(text)
