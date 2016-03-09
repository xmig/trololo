from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description') #'date_started', 'date_finished'
    fields = ('name', 'description') #'date_started', 'date_finished'


admin.site.register(Project, ProjectAdmin)

