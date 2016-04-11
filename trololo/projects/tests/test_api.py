# from projects.views import api_root
# from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
# from django.contrib.auth import get_user_model
# from rest_framework.reverse import reverse
# from rest_framework import status
#
# class TestApi(APITestCase):
#     fixtures = ['data_with_gravatar.json']
#
#     def test_api(self):
#         url = reverse('api')
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = api_root(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data,{
#                  "status": "http://testserver/status/status/",
#                  "tasks": "http://testserver/tasks/",
#                  "users": "http://testserver/users/",
#                  "projects": "http://testserver/projects/"
#             }
#         )
