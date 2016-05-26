from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_activity_emails(recipients, email_body, sender, task_id, task_name):
    for email_addr in recipients:
        send_mail(
            "Changed task #{} {}".format(task_id, task_name),
            email_body,
            sender,
            [email_addr],
            html_message=email_body
        )
