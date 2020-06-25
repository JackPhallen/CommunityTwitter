from django.urls import path
from .views import submission, home

urlpatterns = [
    path('', home.HomeView.as_view(), name="submission_list"),
    path('new/', submission.SubmissionCreateView.as_view(), name="submission_new"),
]