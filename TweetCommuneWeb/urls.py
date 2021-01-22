from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('commune/', include('tweet_commune.urls')),
    re_path(r'^.*/', RedirectView.as_view(url='/commune/', permanent=False), name='index'),
    path('', RedirectView.as_view(url='/commune/', permanent=False), name='index')
]
