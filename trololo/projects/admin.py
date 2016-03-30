from django.contrib import admin
from projects.models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'description', 'visible_by', 'date_started', 'date_finished', 'created_at', 'created_by', 'updated_at', 'updated_by')
    fields = ('name', 'members', 'status', 'description', 'visible_by', 'date_started', 'date_finished')

admin.site.register(Project, ProjectAdmin)



class ProjectCommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'comment')
    fields = ('title', 'project', 'comment')

admin.site.register(ProjectComment, ProjectCommentAdmin)



class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project', 'status', 'type', 'label', 'deadline_date', 'estimate_minutes', 'created_at', 'created_by', 'updated_at', 'updated_by')
    fields = ('name', 'description', 'project', 'members', 'status', 'type', 'label', 'deadline_date', 'estimate_minutes')

admin.site.register(Task, TaskAdmin)



class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'comment')
    fields = ('title','task', 'comment')

admin.site.register(TaskComment, TaskCommentAdmin)



