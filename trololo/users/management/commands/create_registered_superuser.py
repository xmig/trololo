from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from allauth.account.models import EmailAddress, EmailConfirmation
from django.db.models import Q
import datetime
import uuid
from django.utils import timezone
import getpass


class Command(BaseCommand):
    help = '''Create superuser with comfirmed email address.

    Usage: manage.py create_registered_superuser
    '''

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, dest='name', required=True)
        parser.add_argument('--email', type=str, dest='email', required=True)

    def handle(self, *args, **options):
        passwd = getpass.getpass("Enter password:").strip()

        user_model = get_user_model()

        users = user_model.objects.filter(
            Q(username=options['name']) | Q(email=options['email'])
        ).all()

        if users:
            raise CommandError("User with such email/username already exists.")

        u = user_model.objects.create_superuser(
            options['name'], options['email'], passwd
        )

        u.save()

        email_entity = EmailAddress(
            email=options['email'], verified=True,
            primary=True, user=u
        )
        email_entity.save()

        email_confirmation_entity = EmailConfirmation(
            email_address=email_entity,
            created=timezone.now() - datetime.timedelta(days=1),
            sent=timezone.now() - datetime.timedelta(hours=12),
            key=str(uuid.uuid4()).replace('-', '')
        )

        email_confirmation_entity.save()

        self.stdout.write(
            'Successfully created superuser {0} with confirmed email address {1}'.format(
                options['name'], options['email']
            )
        )
