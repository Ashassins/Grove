from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.get_notifications)
]

urlpatterns = format_suffix_patterns(urlpatterns)
