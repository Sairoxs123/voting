from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Contestants(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField("Name", blank=False, null=False, max_length=30)
    position = models.CharField("Position", blank=False, null=False, max_length=30)
    photo = models.ImageField(upload_to='contestants/', null=False)
    votes = models.IntegerField("Votes")

    def __str__(self):
        return self.name

class Students(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField("Name", blank=False, null=False, max_length=30)
    jssid = models.CharField("JSSID", blank=False, null=False, max_length=10)
    grade_sec = models.CharField("Grade", blank=False, max_length=3)

    def __str__(self):
        return self.jssid

class Votes(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name="Student")
    contestant = models.ForeignKey(Contestants, on_delete=models.CASCADE, related_name="Contestant")


class History(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    jssid = models.CharField("JSSID", blank=False, null=False, max_length=10)
    student_name = models.CharField("Name", blank=False, null=False, max_length=50)
    contestant_name = models.CharField("Name of Contestant", blank=False, null=False, max_length=50)
    position = models.CharField("Position", blank=False, null=False, max_length=30)
    date = models.DateField("Date")

