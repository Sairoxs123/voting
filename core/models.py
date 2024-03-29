from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contestants(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField("Name", blank=False, null=False, max_length=30)
    position = models.CharField("Position", blank=False, null=False, max_length=30)
    photo = models.ImageField(upload_to='contestants/', null=False)
    votes = models.IntegerField("Votes")

    def __str__(self):
        return self.name

