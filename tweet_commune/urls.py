from django.urls import path
from .views import submission, home, log

urlpatterns = [
    path('', home.HomeView.as_view(), name="home"),
    path('new/', submission.SubmissionCreateView.as_view(), name="submission_new"),
    path('log/', log.LogListView.as_view(), name="logentry_list"),
    path('log/<slug:pk>', log.LogDetailView.as_view(), name="logentry_detail"),
]