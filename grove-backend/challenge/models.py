from django.db import models
from django.core.validators import MinValueValidator
from users.models import User
from django.contrib import admin
from django.contrib.admin import register

 
class UserChallenge(models.Model):
    src = models.ForeignKey(User, on_delete=models.CASCADE, related_name="src")
    dst = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dst")
    xp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    desc = models.CharField(default="", max_length=255)

    def __repr__(self) -> str:
        return f"{self.src} challenged {self.dst}"


class DailyChallenge(models.Model):
    xp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    desc = models.CharField(default="", max_length=255)


class DailyChallengeCompletion(models.Model):
    daily = models.ForeignKey(DailyChallenge, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


@register(UserChallenge)
class UserChallengeAdmin(admin.ModelAdmin):
    pass


@register(DailyChallenge)
class DailyChallengeAdmin(admin.ModelAdmin):
    pass


