from django.db import connection
from django.conf import settings


def project_del_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        "SELECT sphinx_delete(%s, %s);", [settings.PROJECT_INDEX, kwargs["instance"].id]
    )

    cursor.fetchall()


def project_save_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT sphinx_replace(
            %s, %s,
            ARRAY[
                'name', %s,
                'description', %s,
                'status', %s
            ]
        );
        """, [settings.PROJECT_INDEX] + [getattr(kwargs["instance"], attr) for attr in ('id', 'name', 'description', 'status')]
    )

    cursor.fetchall()


def task_del_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        "SELECT sphinx_delete(%s, %s);", [settings.TASK_INDEX, kwargs['instance'].id]
    )

    cursor.fetchall()


def task_save_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT sphinx_replace(
            %s, %s,
            ARRAY[
                'name', %s,
                'description', %s,
                'label', %s,
                'type', %s
            ]
        );
        """, [settings.TASK_INDEX] + [
            getattr(kwargs["instance"], attr) for attr in ('id', 'name', 'description', 'label', 'type')
        ]
    )

    cursor.fetchall()


def task_comment_del_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        "SELECT sphinx_delete(%s, %s);", [settings.TASK_COMMENT_INDEX, kwargs["instance"].id]
    )

    cursor.fetchall()


def task_comment_save_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT sphinx_replace(
            %s, %s,
            ARRAY[
                'title', %s,
                'comment', %s
            ]
        );
        """, [settings.TASK_COMMENT_INDEX] + [getattr(kwargs["instance"], attr) for attr in ('id', 'title', 'comment')]
    )

    cursor.fetchall()