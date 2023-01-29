from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [path("shake/", views.shake_friend)]

urlpatterns = format_suffix_patterns(urlpatterns)
