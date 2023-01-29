from django.db import models
from users.models import User
from django.contrib.admin import register
from django.contrib import admin


class Notification(models.Model):
    user_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_to")
    content = models.CharField(max_length=1024)
    src = models.CharField(max_length=256, default="System")

    def __str__(self) -> str:
        return f"From {self.src} to {self.user_to}"


@register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass
