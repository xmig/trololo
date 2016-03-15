from django.contrib import admin
from projects.models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'visible_by', 'date_started', 'date_finished')
    fields = ('name', 'description', 'status', 'visible_by', 'date_started', 'date_finished')

admin.site.register(Project, ProjectAdmin)



class ProjectCommentAdmin(admin.ModelAdmin):
    list_display = ('project', 'comment', 'created_at', 'modified_at')
    fields = ('project', 'comment')

admin.site.register(ProjectComment, ProjectCommentAdmin)



class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'type', 'label', 'project', 'created_at', 'modified_at', 'deadline_date', 'estimate_minutes')
    fields = ('name', 'description', 'status', 'type', 'label', 'project', 'deadline_date', 'estimate_minutes')

admin.site.register(Task, TaskAdmin)



class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'comment', 'created_at', 'modified_at')
    fields = ('task', 'comment')

admin.site.register(TaskComment, TaskCommentAdmin)










# class TaskStatusAdmin(admin.ModelAdmin):
#     list_display = ('status',)
#     fields = ('status',)
#
# admin.site.register(TaskStatus, TaskStatusAdmin)
#
#
#
# class TaskTypeAdmin(admin.ModelAdmin):
#     list_display = ('type',)
#     fields = ('type',)
#
# admin.site.register(TaskType, TaskTypeAdmin)
#
#
#
# class TaskLabelAdmin(admin.ModelAdmin):
#     list_display = ('label',)
#     fields = ('label',)
#
# admin.site.register(TaskLabel, TaskLabelAdmin)



