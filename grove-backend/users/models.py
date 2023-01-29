from django.db import models
from django.contrib import admin
from django.contrib.admin import register
from django.db.models import QuerySet


class User(models.Model):
    username = models.CharField(default="", max_length=128)
    first_name = models.CharField(default="", max_length=128)
    last_name = models.CharField(default="", max_length=128)
    status = models.CharField(max_length=256, default="Tending my grove")

    def get_groves(self) -> QuerySet:
        return self.grove_set.all()

    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"


@register(User)
class UserAdmin(admin.ModelAdmin):
    pass
