from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from social.apps.django_app.default.models import UserSocialAuth


class EmailAuthBackend(object):
    """
        Authenticate field username via email address
    """
    def authenticate(self, username=None, password=None):
        user_model = get_user_model()

        # social_ids = [
        #     su.user_id for su in UserSocialAuth.objects.all()
        # ]

        try:
            user = user_model.objects.filter(email=username).all()
            # .exclude(id__in=social_ids) \
        except user_model.DoesNotExist:
            return None

        pwd_valid = check_password(password, user.password)

        return user if pwd_valid else None

    def get_user(self, user_id):
        user_model = get_user_model()

        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None