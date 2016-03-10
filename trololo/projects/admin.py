from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description', 'status', 'visible_by') #'date_started', 'date_finished'
    fields = ('name', 'description', 'status', 'visible_by') #'date_started', 'date_finished'


admin.site.register(Project, ProjectAdmin)



class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description', 'status', 'type', 'label', 'project') #'created_at', 'modified_at', 'deadline_date', 'estimate_minutes'
    fields = ('name', 'description', 'status', 'type', 'label', 'project') #'created_at', 'modified_at', 'deadline_date', 'estimate_minutes'


admin.site.register(Task, TaskAdmin)



class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'description', 'id')
    fields = ('status', 'description')

admin.site.register(TaskStatus, TaskStatusAdmin)



class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('description', 'type', 'id')
    fields = ('description', 'type')


admin.site.register(TaskType, TaskTypeAdmin)


class TaskLabelAdmin(admin.ModelAdmin):
    list_display = ('label', 'description', 'id')
    fields = ('label', 'description')

admin.site.register(TaskLabel, TaskLabelAdmin)



class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'comment', 'id')
    fields = ('task', 'comment')


admin.site.register(TaskComment, TaskCommentAdmin)