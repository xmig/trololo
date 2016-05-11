from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q

from projects.models import Project, Task, TaskComment
from projects.signals import project_save_callback, task_save_callback, task_comment_save_callback


class Command(BaseCommand):
    help = '''Create initial index for sphinx search for projects, tasks and task comments

    Usage: manage.py sphinx_initial_index
    '''

    # def add_arguments(self, parser):
    #     parser.add_argument('--name', type=str, dest='name', required=True)
    #     parser.add_argument('--email', type=str, dest='email', required=True)

    def handle(self, *args, **options):
        for pr in Project.objects.all():
            project_save_callback(instance=pr)

        for task in Task.objects.all():
            task_save_callback(instance=task)

        for tc in TaskComment.objects.all():
            task_comment_save_callback(instance=tc)

        self.stdout.write('Sphinx index has been created')
