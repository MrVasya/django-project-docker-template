from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=300)

    def __str__(self):
        return self.name
