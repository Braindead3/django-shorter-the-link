from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    url = models.CharField(max_length=100)
    short_url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
