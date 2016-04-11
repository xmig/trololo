# from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
# from django.contrib.auth import get_user_model
# from users.views import (
#     UserProfile, EmailVerificationSentView, AccountConfirmEmailView, SingleUser, UserListView
# )
# from PIL import Image
# import tempfile, os, mock
# from rest_framework import status
# from rest_framework.reverse import reverse
# from urlparse import urlparse
# from rest_auth.registration.views import VerifyEmailView
#
#
# class TestUserProfileGet(APITestCase):
#     fixtures = ['data.json']
#
#     def test_get_user_profile(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='user')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         self.assertEqual(
#             response.data,
#             {
#                 'username': u'user', 'first_name': u'', 'last_name': u'', 'specialization': u'',
#                 'photo': u'http://www.curiousinkling.com/img/trololo/trololo-t-shirts-005DES.gif',
#                 'is_active': True, 'email': u'maxellort@gmail.com',
#                 'is_superuser': False, 'is_staff': False, 'last_login': u'2016-03-09T13:10:20.662000Z',
#                 'department': u'', 'detailed_info': u'', u'id': 1, 'date_joined': u'2016-03-09T12:46:26.556000Z',
#                 'projects': [], 'use_gravatar': False,'url': u'http://testserver/users/1/', 'tasks': []
#             }
#         )
#
#     def test_get_user_after_update(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='user')
#
#         factory = APIRequestFactory()
#         image = Image.new('RGB', (100, 100))
#         tmp_file = tempfile.NamedTemporaryFile(prefix='logo', suffix='.jpg')
#         image.save(tmp_file)
#         tmp_file.seek(0)
#
#         request = factory.put(url, {'photo': tmp_file, 'department': 'FBI'}, format='multipart')
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         self.assertEqual(user.department, 'FBI')
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#         self.assertTrue(user.photo.name.startswith('user_{0}/logo'.format(user.id)))
#
#         url = reverse('users:user_profile')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         ETALON = {
#             'username': u'user', 'first_name': u'', 'last_name': u'', 'specialization': u'',
#             'photo': 'http://testserver/media/user_{0}/{1}'.format(user.id, 'logo.jpg'), 'is_active': True,
#             'email': u'maxellort@gmail.com', 'is_superuser': False, 'is_staff': False,
#             'last_login': u'2016-03-09T13:10:20.662000Z', 'department': u'FBI', 'detailed_info': u'',
#             u'id': 1, 'date_joined': u'2016-03-09T12:46:26.556000Z', 'projects': [], 'use_gravatar': False,
#             'url': u'http://testserver/users/1/', 'tasks': []
#         }
#
#         self.assertEqual(response.data, ETALON)
#
#
# class TestUserProfileUpdate(APITestCase):
#     fixtures = ['data.json']
#
#     def test_user_photo(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='user')
#
#         factory = APIRequestFactory()
#         image = Image.new('RGB', (150, 120))
#         tmp_file = tempfile.NamedTemporaryFile(prefix='logo', suffix='.jpg')
#         image.save(tmp_file)
#         tmp_file.seek(0)
#         request = factory.put(url, {'photo': tmp_file, 'department': 'python'}, format='multipart')
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         self.assertTrue(user.department == 'python')
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#         self.assertTrue(user.photo.name.startswith('user_{0}/{1}'.format(user.id, 'logo.jpg')))
#
#         user = get_user_model().objects.get(username='user')
#         # check image resize
#         self.assertEqual(user.photo.width, 112)
#         self.assertEqual(user.photo.height, int(round((112.0 / 150) * 120)))
#
#     def test_user_first_name_update(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='user')
#
#         factory =APIRequestFactory()
#         request = factory.put(url, {'first_name': 'John'}, format='multipart')
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#         self.assertTrue(user.first_name == 'John')
#
#
#     def test_last_name_update(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='user')
#
#         factory =APIRequestFactory()
#         request = factory.put(url, {'last_name': 'Doy'}, format='multipart')
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         self.assertTrue(user.last_name == 'Doy')
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#
#
#     def test_specialization_update(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='user')
#
#         factory =APIRequestFactory()
#         request = factory.put(url, {'specialization': 'developer'}, format='multipart')
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         self.assertTrue(user.specialization == 'developer')
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#
#
#     def test_detailed_info_specialization_update(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='user')
#
#         factory =APIRequestFactory()
#         request = factory.put(url, {'detailed_info': 'born in USA', 'specialization': 'developer'}, format='multipart')
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         self.assertTrue(user.detailed_info == 'born in USA', user.specialization == 'developer')
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#
#
# class TestEmailVerificationSentView(APITestCase):
#     def test_email_verification_sent(self):
#         url = reverse('account_email_verification_sent')
#         factory = APIRequestFactory()
#
#         request = factory.get(url)
#         response = EmailVerificationSentView.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, "Verification email has been sent.")
#
#
# class RequestsPost(object):
#     def __init__(self, status_code=200, data={}, raw=''):
#         self.status_code = status_code
#         self.data = data
#         self.raw = raw
#
#
# class RequestsRequest(object):
#     def __init__(self, url_name=''):
#         self.url_name = url_name
#
#     def post(self, url, *args, **kwargs):
#         post_resp = RequestsPost()
#         view_url = reverse(self.url_name)
#
#         if urlparse(url).path == view_url:
#             factory = APIRequestFactory()
#
#             request = factory.post(view_url, kwargs.get('json', {}))
#             response = VerifyEmailView.as_view()(request, **kwargs['json'])
#             post_resp.status_code = response.status_code
#
#         return post_resp
#
#
# class TestAccountConfirmView(APITestCase):
#     fixtures = ['data.json']
#
#     def setUp(self):
#         super(TestAccountConfirmView, self).setUp()
#         self.requests_mock = mock.patch(
#             'users.views.requests.post',
#             new=RequestsRequest('registration:rest_verify_email').post
#         )
#         self.requests_mock.start()
#
#     def tearDown(self):
#         super(TestAccountConfirmView, self).tearDown()
#         self.requests_mock.stop()
#
#     def test_account_confirm_email(self):
#         key = "ihoeqvcuyliphh4p1zexgcl4vh4fksizkbblfyeuwcfszot1vmyft1nakglmvgmd"
#         url = reverse('account_confirm_email', kwargs={"key": key})
#
#         factory = APIRequestFactory()
#
#         request = factory.get(url)
#         response = AccountConfirmEmailView.as_view()(request, key)
#
#         response.render()
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(
#             response.content,
#             '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>registration complete</title>
# </head>
# <body>
#
# <b>REGISTRATION COMPLETED</b>
#
# </body>
# </html>'''
#         )
#
#
# class TestGetSingleUser(APITestCase):
#     fixtures = ['data.json']
#
#     def test_get_existed_user(self):
#         url = reverse('users:single_user', kwargs={'id': '1'})
#         user = get_user_model().objects.get(username='user')
#
#         factory = APIRequestFactory()
#         request = factory.get(url, format='json')
#         force_authenticate(request, user=user)
#
#         response = SingleUser.as_view()(request, '1')
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data,
#             {
#                 'username': u'user', 'first_name': u'', 'last_name': u'', 'specialization': u'',
#                 'photo': u'http://www.curiousinkling.com/img/trololo/trololo-t-shirts-005DES.gif',
#                 'is_active': True, 'email': u'maxellort@gmail.com',
#                 'is_superuser': False, 'is_staff': False, 'last_login': u'2016-03-09T13:10:20.662000Z',
#                 'department': u'', 'detailed_info': u'', u'id': 1, 'date_joined': u'2016-03-09T12:46:26.556000Z',
#                 'projects': [], 'use_gravatar': False, 'url': u'http://testserver/users/1/', 'tasks': []
#             }
#         )
#
#     def test_get_not_existed_user(self):
#         url = reverse('users:single_user', kwargs={'id': '100'})
#         user = get_user_model().objects.get(username='user')
#
#         factory = APIRequestFactory()
#         request = factory.get(url, format='json')
#         force_authenticate(request, user=user)
#
#         response = SingleUser.as_view()(request, '100')
#
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#
# class TestUserList(APITestCase):
#     fixtures = ['data.json']
#
#     def test_get_users_list(self):
#         url = reverse('users:user_list') + '?name=use&logged_min=2016-03-09T13:10:19&logged_max=2016-03-10T13:11:19'
#
#         user = get_user_model().objects.get(username='user')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#         force_authenticate(request, user=user)
#
#         response = UserListView.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data['results'],
#             [
#                 {
#                     'username': u'user', 'first_name': u'', 'last_name': u'', 'specialization': u'',
#                     'photo': u'http://www.curiousinkling.com/img/trololo/trololo-t-shirts-005DES.gif',
#                     'is_active': True, 'email': u'maxellort@gmail.com',
#                     'is_superuser': False, 'is_staff': False, 'last_login': u'2016-03-09T13:10:20.662000Z',
#                     'department': u'', 'detailed_info': u'', u'id': 1, 'date_joined': u'2016-03-09T12:46:26.556000Z',
#                     'projects': [],'use_gravatar': False, 'url': u'http://testserver/users/1/', 'tasks': []
#                 }
#             ]
#         )
#
#     # TODO: update tests
#     def test_get_users_list_by_project(self):
#         url = reverse('users:user_list') + '?project=1&name=use'
#
#         user = get_user_model().objects.get(username='user')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#         force_authenticate(request, user=user)
#
#         response = UserListView.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['results'], [])
#
#     def test_get_users_list_by_task(self):
#         url = reverse('users:user_list') + '?task=1&name=use'
#
#         user = get_user_model().objects.get(username='user')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#         force_authenticate(request, user=user)
#
#         response = UserListView.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['results'], [])
#
#     def test_get_user_list_filter_by_loggerin(self):
#         url = reverse('users:user_list') + '?logged_min=2016-03-09T13:10:21'
#
#         user = get_user_model().objects.get(username='user')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#         force_authenticate(request, user=user)
#
#         response = UserListView.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['results'], [])
#
#
# class TestUserProfileGravatar(APITestCase):
#     fixtures = ['data_with_gravatar.json']
#
#     def test_get_user_profile_with_gravatar(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         res = {
#             'username': u'yura', 'first_name': u'yura', 'last_name': u'', 'specialization': u'',
#             'photo': "http://www.gravatar.com/avatar/b4c20c59303507f4c03435a0877ee46b?s=50&d=http%3A%2F%2Fwww."
#                      "curiousinkling.com%2Fimg%2Ftrololo%2Ftrololo-t-shirts-005DES.gif", 'is_active': True,
#             'email': u'yura@example.com',
#             'is_superuser': True, 'is_staff': True, 'last_login': u'2016-03-18T13:26:04.553000Z',
#             'department': u'', 'detailed_info': u'', u'id': 1, 'date_joined': u'2016-03-18T09:54:08.108000Z',
#             'projects': [u'http://testserver/projects/1/'], 'use_gravatar': True,
#             'url': u'http://testserver/users/1/', 'tasks': []
#         }
#
#         for k, v in res.iteritems():
#             self.assertEqual(response.data[k], v)
#
#
# class TestUserProfileAddTasks(APITestCase):
#     fixtures = ['data_with_gravatar.json']
#
#     def test_get_user_profile_add_tasks(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.put(url, {'tasks': ["http://testserver/tasks/1/"]}, format='multipart')
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#
#         ETALON = {
#             'username': u'yura', 'first_name': u'yura', 'last_name': u'', 'specialization': u'',
#             'photo': "http://www.gravatar.com/avatar/b4c20c59303507f4c03435a0877ee46b?s=50&d=http%3A%2F%2Fwww."
#                      "curiousinkling.com%2Fimg%2Ftrololo%2Ftrololo-t-shirts-005DES.gif", 'is_active': True,
#             'email': u'yura@example.com',
#             'is_superuser': True, 'is_staff': True, 'last_login': u'2016-03-18T13:26:04.553000Z',
#             'department': u'', 'detailed_info': u'', u'id': 1, 'date_joined': u'2016-03-18T09:54:08.108000Z',
#             'projects': [u'http://testserver/projects/1/'], 'use_gravatar': True,
#             'url': u'http://testserver/users/1/', 'tasks': [
#                 u"http://testserver/tasks/1/"
#             ]
#         }
#         for k in ETALON:
#             self.assertEqual(response.data[k], ETALON[k])
#
#
#
# class TestUserProfileAddProjects(APITestCase):
#     fixtures = ['data_with_gravatar.json']
#
#     def test_get_user_profile_add_projects(self):
#         url = reverse('users:user_profile')
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.put(url, {'projects': ["http://testserver/projects/1/"]},
#                               format='multipart'
#                               )
#
#         force_authenticate(request, user=user)
#         response = UserProfile.as_view()(request)
#
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#
#         ETALON = {
#             'username': u'yura', 'first_name': u'yura', 'last_name': u'', 'specialization': u'',
#             'photo': "http://www.gravatar.com/avatar/b4c20c59303507f4c03435a0877ee46b?s=50&d=http%3A%2F%2Fwww."
#                      "curiousinkling.com%2Fimg%2Ftrololo%2Ftrololo-t-shirts-005DES.gif", 'is_active': True,
#             'email': u'yura@example.com',
#             'is_superuser': True, 'is_staff': True, 'last_login': u'2016-03-18T13:26:04.553000Z',
#             'department': u'', 'detailed_info': u'', u'id': 1, 'date_joined': u'2016-03-18T09:54:08.108000Z',
#             'projects': [u'http://testserver/projects/1/'], 'use_gravatar': True,
#             'url': u'http://testserver/users/1/', 'tasks': []
#         }
#
#         for k in ETALON:
#             self.assertEqual(response.data[k], ETALON[k])
