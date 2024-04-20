from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Contestants)

class ContestantsAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'position', 'votes']
    search_fields = ['name', 'position']
    list_filter = ['position']

@admin.register(Students)

class StudentAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "jssid", "name", "grade_sec"]
    search_fields = ["jssid", "name"]
    list_filter = ["grade_sec"]

@admin.register(Votes)

class VotesAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "student", "contestant"]


@admin.register(History)

class HistoryAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "jssid", "student_name", "contestant_name", "position", "date"]
    list_filter = ["date"]
