from django.db import connection


def project_del_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        "SELECT sphinx_delete('project_rt', %s);", [kwargs["instance"].id]
    )

    cursor.fetchall()


def project_save_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT sphinx_replace(
            'project_rt', %s,
            ARRAY[
                'name', %s,
                'description', %s,
                'status', %s
            ]
        );
        """, [getattr(kwargs["instance"], attr) for attr in ('id', 'name', 'description', 'status')]
    )

    cursor.fetchall()


def task_del_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        "SELECT sphinx_delete('task_rt', %s);", [kwargs['instance'].id]
    )

    cursor.fetchall()


def task_save_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT sphinx_replace(
            'task_rt', %s,
            ARRAY[
                'name', %s,
                'description', %s,
                'label', %s,
                'type', %s
            ]
        );
        """, [
            getattr(kwargs["instance"], attr) for attr in ('id', 'name', 'description', 'label', 'type')
        ]
    )

    cursor.fetchall()


def task_comment_del_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        "SELECT sphinx_delete('task_comment_rt', %s);", [kwargs["instance"].id]
    )

    cursor.fetchall()


def task_comment_save_callback(**kwargs):
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT sphinx_replace(
            'task_comment_rt', %s,
            ARRAY[
                'title', %s,
                'comment', %s
            ]
        );
        """, [getattr(kwargs["instance"], attr) for attr in ('id', 'title', 'comment')]
    )

    cursor.fetchall()