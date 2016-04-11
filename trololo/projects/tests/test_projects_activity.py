# from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
# from rest_framework.reverse import reverse
# from django.contrib.auth import get_user_model
# from projects.views import (
#     ProjectActivity
# )
# from projects.models import Project
# from collections import OrderedDict
#
#
# class TestProjectActivities(APITestCase):
#     fixtures = ['activity_test.json']
#
#     def __get_project_activities(self, expected, url_params={}, show_type='a'):
#         user = get_user_model().objects.get(pk=1)
#         factory = APIRequestFactory()
#         view = ProjectActivity.as_view()
#         project_id = 2
#         # show_type = 'p'
#         url = reverse('projects:project_activity', kwargs={'id': project_id, 'show_type':show_type})
#
#         request = factory.get(url, url_params)
#         force_authenticate(request, user=user)
#         response = view(request, project_id, show_type)
#
#         self.assertEquals(response.data, expected)
#
#     def test_get_project_activities(self):
#         url_params = {}
#         expected = [
#             OrderedDict(
#                 [('id', 21), ('message', u'create new task "task6"'), ('created_at', u'2016-03-28T12:39:22.504000Z'),
#                  ('updated_at', u'2016-03-28T12:39:22.504000Z'), ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 20), ('message', u'edit task Name: "task5" ==> "task51"'),
#                          ('created_at', u'2016-03-28T12:38:56.241000Z'), ('updated_at', u'2016-03-28T12:38:56.241000Z'),
#                          ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 19), ('message', u'edit task Name: "task4" ==> "task41"'),
#                  ('created_at', u'2016-03-28T12:38:45.547000Z'), ('updated_at', u'2016-03-28T12:38:45.547000Z'),
#                  ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 18), ('message', u'edit project'), ('created_at', u'2016-03-22T12:56:54.253000Z'),
#                  ('updated_at', u'2016-03-22T12:56:54.254000Z'), ('created_by', None), ('updated_by', None)]
#             ),
#             OrderedDict(
#                 [('id', 15), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:52:23.235000Z'),
#                  ('updated_at', u'2016-03-18T14:52:23.235000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 10), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:08:13.143000Z'),
#                  ('updated_at', u'2016-03-18T14:08:13.143000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 5), ('message', u'edit project "project2"'), ('created_at', u'2016-03-18T13:30:55.248000Z'),
#                  ('updated_at', u'2016-03-18T13:30:55.248000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 2), ('message', u'create new project "project2"'),
#                  ('created_at', u'2016-03-18T10:56:40.382000Z'), ('updated_at', u'2016-03-18T10:56:40.382000Z'),
#                  ('created_by', 1), ('updated_by', 1)]
#             )
#         ]
#         self.__get_project_activities(expected, url_params)
#
#     def test_get_only_project_activities(self):
#         url_params = {}
#         show_type = 'p'
#         expected = [
#             OrderedDict(
#                 [('id', 18), ('message', u'edit project'), ('created_at', u'2016-03-22T12:56:54.253000Z'),
#                  ('updated_at', u'2016-03-22T12:56:54.254000Z'), ('created_by', None), ('updated_by', None)]
#             ),
#             OrderedDict(
#                 [('id', 15), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:52:23.235000Z'),
#                  ('updated_at', u'2016-03-18T14:52:23.235000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 10), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:08:13.143000Z'),
#                  ('updated_at', u'2016-03-18T14:08:13.143000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 5), ('message', u'edit project "project2"'), ('created_at', u'2016-03-18T13:30:55.248000Z'),
#                  ('updated_at', u'2016-03-18T13:30:55.248000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 2), ('message', u'create new project "project2"'),
#                  ('created_at', u'2016-03-18T10:56:40.382000Z'), ('updated_at', u'2016-03-18T10:56:40.382000Z'),
#                  ('created_by', 1), ('updated_by', 1)]
#             )
#         ]
#         self.__get_project_activities(expected, url_params, show_type)
#
#     def test_get_only_task_activities(self):
#         url_params = {}
#         show_type = 't'
#         expected = [
#             OrderedDict(
#                 [('id', 21), ('message', u'create new task "task6"'), ('created_at', u'2016-03-28T12:39:22.504000Z'),
#                  ('updated_at', u'2016-03-28T12:39:22.504000Z'), ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 20), ('message', u'edit task Name: "task5" ==> "task51"'),
#                          ('created_at', u'2016-03-28T12:38:56.241000Z'), ('updated_at', u'2016-03-28T12:38:56.241000Z'),
#                          ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 19), ('message', u'edit task Name: "task4" ==> "task41"'),
#                  ('created_at', u'2016-03-28T12:38:45.547000Z'), ('updated_at', u'2016-03-28T12:38:45.547000Z'),
#                  ('created_by', 3), ('updated_by', 3)]
#             )
#         ]
#         self.__get_project_activities(expected, url_params, show_type)
#
#     def test_get_project_activities_filter_by_message_like(self):
#         url_params = {"message_like": "create"}
#         expected = [
#             OrderedDict(
#                 [('id', 21), ('message', u'create new task "task6"'), ('created_at', u'2016-03-28T12:39:22.504000Z'),
#                  ('updated_at', u'2016-03-28T12:39:22.504000Z'), ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 2), ('message', u'create new project "project2"'),
#                  ('created_at', u'2016-03-18T10:56:40.382000Z'), ('updated_at', u'2016-03-18T10:56:40.382000Z'),
#                  ('created_by', 1), ('updated_by', 1)]
#             )
#         ]
#         self.__get_project_activities(expected, url_params)
#
#     def test_get_project_activities_filter_by_message(self):
#         url_params = {"message": "edit project"}
#         expected = [
#             OrderedDict(
#                 [('id', 18), ('message', u'edit project'), ('created_at', u'2016-03-22T12:56:54.253000Z'),
#                  ('updated_at', u'2016-03-22T12:56:54.254000Z'), ('created_by', None), ('updated_by', None)]
#             )
#         ]
#         self.__get_project_activities(expected, url_params)
#
#     def test_get_project_activities_filter_by_date(self):
#         url_params = {"date_0": "2016-03-18 14:00:00", "date_1": "2016-03-18 15:00:00"}
#         expected = [
#             OrderedDict(
#                 [('id', 15), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:52:23.235000Z'),
#                  ('updated_at', u'2016-03-18T14:52:23.235000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 10), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:08:13.143000Z'),
#                  ('updated_at', u'2016-03-18T14:08:13.143000Z'), ('created_by', 1), ('updated_by', 1)]
#             )
#         ]
#         self.__get_project_activities(expected, url_params)
#
#     def test_get_project_activities_filter_by_current_user(self):
#         url_params = {"for_cu":"1"}
#         expected = [
#             OrderedDict(
#                 [('id', 15), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:52:23.235000Z'),
#                  ('updated_at', u'2016-03-18T14:52:23.235000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 10), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:08:13.143000Z'),
#                  ('updated_at', u'2016-03-18T14:08:13.143000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 5), ('message', u'edit project "project2"'), ('created_at', u'2016-03-18T13:30:55.248000Z'),
#                  ('updated_at', u'2016-03-18T13:30:55.248000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 2), ('message', u'create new project "project2"'),
#                  ('created_at', u'2016-03-18T10:56:40.382000Z'), ('updated_at', u'2016-03-18T10:56:40.382000Z'),
#                  ('created_by', 1), ('updated_by', 1)]
#             ),
#         ]
#         self.__get_project_activities(expected, url_params)
#
#     def test_get_project_activities_sorting_asc(self):
#         url_params = {"ordering": "message,created_at"}
#         expected = [
#             OrderedDict(
#                 [('id', 2), ('message', u'create new project "project2"'),
#                  ('created_at', u'2016-03-18T10:56:40.382000Z'), ('updated_at', u'2016-03-18T10:56:40.382000Z'),
#                  ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 21), ('message', u'create new task "task6"'), ('created_at', u'2016-03-28T12:39:22.504000Z'),
#                  ('updated_at', u'2016-03-28T12:39:22.504000Z'), ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 18), ('message', u'edit project'), ('created_at', u'2016-03-22T12:56:54.253000Z'),
#                  ('updated_at', u'2016-03-22T12:56:54.254000Z'), ('created_by', None), ('updated_by', None)]
#             ),
#             OrderedDict(
#                 [('id', 5), ('message', u'edit project "project2"'), ('created_at', u'2016-03-18T13:30:55.248000Z'),
#                  ('updated_at', u'2016-03-18T13:30:55.248000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 10), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:08:13.143000Z'),
#                  ('updated_at', u'2016-03-18T14:08:13.143000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 15), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:52:23.235000Z'),
#                  ('updated_at', u'2016-03-18T14:52:23.235000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 19), ('message', u'edit task Name: "task4" ==> "task41"'),
#                  ('created_at', u'2016-03-28T12:38:45.547000Z'), ('updated_at', u'2016-03-28T12:38:45.547000Z'),
#                  ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 20), ('message', u'edit task Name: "task5" ==> "task51"'),
#                          ('created_at', u'2016-03-28T12:38:56.241000Z'), ('updated_at', u'2016-03-28T12:38:56.241000Z'),
#                          ('created_by', 3), ('updated_by', 3)]
#             )
#         ]
#         self.__get_project_activities(expected, url_params)
#
#     def test_get_project_activities_sorting_desc(self):
#         url_params = {"ordering": "-message,-created_at"}
#         expected = [
#             OrderedDict(
#                 [('id', 20), ('message', u'edit task Name: "task5" ==> "task51"'),
#                          ('created_at', u'2016-03-28T12:38:56.241000Z'), ('updated_at', u'2016-03-28T12:38:56.241000Z'),
#                          ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 19), ('message', u'edit task Name: "task4" ==> "task41"'),
#                  ('created_at', u'2016-03-28T12:38:45.547000Z'), ('updated_at', u'2016-03-28T12:38:45.547000Z'),
#                  ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 15), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:52:23.235000Z'),
#                  ('updated_at', u'2016-03-18T14:52:23.235000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 10), ('message', u'edit project "projectb"'), ('created_at', u'2016-03-18T14:08:13.143000Z'),
#                  ('updated_at', u'2016-03-18T14:08:13.143000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 5), ('message', u'edit project "project2"'), ('created_at', u'2016-03-18T13:30:55.248000Z'),
#                  ('updated_at', u'2016-03-18T13:30:55.248000Z'), ('created_by', 1), ('updated_by', 1)]
#             ),
#             OrderedDict(
#                 [('id', 18), ('message', u'edit project'), ('created_at', u'2016-03-22T12:56:54.253000Z'),
#                  ('updated_at', u'2016-03-22T12:56:54.254000Z'), ('created_by', None), ('updated_by', None)]
#             ),
#             OrderedDict(
#                 [('id', 21), ('message', u'create new task "task6"'), ('created_at', u'2016-03-28T12:39:22.504000Z'),
#                  ('updated_at', u'2016-03-28T12:39:22.504000Z'), ('created_by', 3), ('updated_by', 3)]
#             ),
#             OrderedDict(
#                 [('id', 2), ('message', u'create new project "project2"'),
#                  ('created_at', u'2016-03-18T10:56:40.382000Z'), ('updated_at', u'2016-03-18T10:56:40.382000Z'),
#                  ('created_by', 1), ('updated_by', 1)]
#             )
#         ]
#         self.__get_project_activities(expected, url_params)
#
