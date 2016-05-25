from django.contrib import admin
from projects.models import *



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'description', 'visible_by', 'date_started', 'date_finished', 'created_at', 'created_by', 'updated_at', 'updated_by')
    fields = ('name', 'members', 'status', 'description', 'visible_by', 'date_started', 'date_finished')
    list_filter = ('name', 'status', 'visible_by', 'date_started', 'date_finished', 'created_at', 'created_by', 'updated_at', 'updated_by')

admin.site.register(Project, ProjectAdmin)



class ProjectCommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'comment')
    fields = ('title', 'project', 'comment')
    list_filter = ('title','project')

admin.site.register(ProjectComment, ProjectCommentAdmin)



class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project', 'status', 'type', 'label', 'deadline_date', 'estimate_minutes', 'created_at', 'created_by', 'updated_at', 'updated_by')
    fields = ('name', 'description', 'project', 'assigned_member', 'members', 'status', 'type', 'label', 'deadline_date', 'estimate_minutes')
    list_filter = ('name', 'project', 'status', 'type', 'label', 'deadline_date', 'estimate_minutes', 'created_at', 'created_by', 'updated_at', 'updated_by')

admin.site.register(Task, TaskAdmin)



class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'comment')
    fields = ('title','task', 'comment')
    list_filter = ('title','task')

admin.site.register(TaskComment, TaskCommentAdmin)



