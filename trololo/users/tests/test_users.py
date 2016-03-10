from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from users.views import UserProfile


class TestUserProfileGet(APITestCase):
    fixtures = ['data.json']

    def test_get_user_profile(self):
        url = reverse('users:user_profile')
        user = get_user_model().objects.get(username='user')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = UserProfile.as_view()(request)

        self.assertEqual(
            response.data,
            {
                'username': u'user', 'first_name': u'', 'last_name': u'', 'specialization': u'',
                'photo': None, 'is_active': True, 'email': u'maxellort@gmail.com',
                'is_superuser': False, 'is_staff': False, 'last_login': u'2016-03-09T13:10:20.662000Z',
                'department': u'', 'detailed_info': u'', u'id': 1, 'date_joined': u'2016-03-09T12:46:26.556000Z'
            }
        )