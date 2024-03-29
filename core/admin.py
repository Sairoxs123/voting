from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Contestants)

class ContestantsAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'position', 'votes']
    search_fields = ['name', 'position']
    list_filter = ['position']

