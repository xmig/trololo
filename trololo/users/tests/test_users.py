from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from users.views import UserProfile
from PIL import Image
import tempfile
from rest_framework import status


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

class TestUserProfileUpdate(APITestCase):
    fixtures = ['data.json']

    def test_user_photo(self):
        url = reverse('users:user_profile')
        user = get_user_model().objects.get(username='user')

        factory = APIRequestFactory()
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(prefix='logo', suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        request = factory.put(url, {'photo': tmp_file, 'department': 'python'}, format='multipart')

        force_authenticate(request, user=user)
        response = UserProfile.as_view()(request)

        self.assertTrue(user.department == 'python')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertTrue(user.photo.name.startswith('user_{0}/logo'.format(user.id)))


    def test_user_first_name(self):
        url = reverse('users:user_profile')
        user = get_user_model().objects.get(username='user')

        factory =APIRequestFactory()
        request = factory.put(url, {'first_name': 'Jon'}, format='multipart')

        force_authenticate(request, user=user)
        response = UserProfile.as_view()(request)

        self.assertTrue(user.first_name == 'Jon')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def last_name(self):
        url = reverse('users:user_profile')
        user = get_user_model().objects.get(username='user')

        factory =APIRequestFactory()
        request = factory.put(url, {'first_name': 'Doy'}, format='multipart')

        force_authenticate(request, user=user)
        response = UserProfile.as_view()(request)

        self.assertTrue(user.first_name == 'Doy')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def specialization(self):
        url = reverse('users:user_profile')
        user = get_user_model().objects.get(username='user')

        factory =APIRequestFactory()
        request = factory.put(url, {'specialization': 'developer'}, format='multipart')

        force_authenticate(request, user=user)
        response = UserProfile.as_view()(request)

        self.assertTrue(user.specialization == 'developer')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def detailed_info_specialization(self):
        url = reverse('users:user_profile')
        user = get_user_model().objects.get(username='user')

        factory =APIRequestFactory()
        request = factory.put(url, {'detailed_info': 'born in USA', 'specialization': 'developer'}, format='multipart')

        force_authenticate(request, user=user)
        response = UserProfile.as_view()(request)

        self.assertTrue(user.detailed_info == 'born in USA', user.specialization == 'developer')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

