from django.apps import AppConfig
from django.db.models.signals import post_delete, post_save
from projects.signals import (
    project_del_callback, project_save_callback, task_save_callback,
    task_del_callback, task_comment_save_callback, task_comment_del_callback
)
from django.conf import settings


class ProjectsAppConfig(AppConfig):
    name = "projects"

    def __init__(self, *args, **kwargs):
        super(ProjectsAppConfig, self).__init__(*args, **kwargs)
        self.ready_runned = False

    def ready(self):
        if not getattr(self, 'ready_runned') and settings.USE_GLOBAL_SEARCH:
            Project = self.get_model('Project')
            Task = self.get_model('Task')
            TaskComment = self.get_model("TaskComment")

            post_delete.connect(project_del_callback, Project)
            post_save.connect(project_save_callback, Project)
            post_save.connect(task_save_callback, Task)
            post_delete.connect(task_del_callback, Task)
            post_save.connect(task_comment_save_callback, TaskComment)
            post_delete.connect(task_comment_del_callback, TaskComment)

            self.ready_runned = True