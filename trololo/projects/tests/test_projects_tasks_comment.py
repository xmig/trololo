# from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
# from django.contrib.auth import get_user_model
# from projects.views import ProjectCommentList, ProjectCommentDetail, TaskCommentList, TaskCommentDetail
# from rest_framework.reverse import reverse
# from rest_framework import status
#
#
#
# class TestProjectComment(APITestCase):
#     fixtures = ['project_comments.json']
#
#     def test_project_comment(self):
#             url = reverse('comments_projects:comments')
#             user = get_user_model().objects.get(username='yura')
#
#             factory = APIRequestFactory()
#             request = factory.get(url)
#
#             force_authenticate(request, user=user)
#             response = ProjectCommentList.as_view()(request)
#
#             self.assertEqual(response.status_code, status.HTTP_200_OK)
#             self.assertEqual(
#                 response.data['results'],
#                 [
#                     {
#                         'title': u'rr', 'comment': u'second comment', 'id': 2,
#                         'project': u'http://testserver/projects/1/', 'created_by': u'http://testserver/users/1/',
#                         'created_at': u'2016-04-07T14:34:09.932000Z', 'updated_by': u'http://testserver/users/1/',
#                         'updated_at': u'2016-04-07T14:34:09.932000Z', 'activity': [9]
#                     },
#                     {
#                         'title':u'yy', 'comment': u'4', 'id': 4, 'project': u'http://testserver/projects/1/',
#                         'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T14:39:08.116000Z',
#                         'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T14:39:08.116000Z',
#                         'activity': [9]
#                     },
#                     {
#                         'title': u'er', 'comment': u'555', 'id': 5, 'project': u'http://testserver/projects/1/',
#                         'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T14:57:20.069000Z',
#                         'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T14:57:20.069000Z',
#                         'activity': [60]
#                     },
#                     {
#                         'title': u'34', 'comment': u'4444444', 'id': 6, 'project': u'http://testserver/projects/1/',
#                         'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T15:21:54.110000Z',
#                         'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T15:21:54.110000Z',
#                         'activity': [61]
#                     }
#                 ]
#             )
#
#     def test_project_comment_add(self):
#         url = reverse('comments_projects:comments')
#
#         self.client.login(username='yura', password='123')
#         response = self.client.post(url, data=
#             {
#                 'title': 'first name', 'comment': 'treee',
#                 'project': 'http://testserver/projects/1/'
#             }
#         )
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#         ETALON = {
#             'title': u'first name', 'comment': u'treee', 'id': 8,
#             'project': u'http://testserver/projects/1/',
#             'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T15:21:54.110000Z',
#             'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T15:21:54.110000Z',
#             'activity': [63]
#         }
#
#         for key in response.data:
#             if key in ['created_at', 'updated_at']:
#                 self.assertIsNotNone(response.data[key])
#             else:
#                 self.assertEqual(ETALON[key], response.data[key])
#
#     def test_add_project_comment_error(self):
#         url = reverse('comments_projects:comments')
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#
#         request = factory.post(url,
#                                {'title': u'first name', 'comment': u'treee',
#                                 'project': u'http://testserver/projects/4/'
#                                }
#         )
#
#         force_authenticate(request, user=user)
#         response = ProjectCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_project_comment_not_found(self):
#         url = reverse('comments_projects:comments_detail', kwargs={'pk': '50'})
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response =ProjectCommentDetail.as_view()(request, '50')
#
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_project_comment_put(self):
#         url = reverse('comments_projects:comments_detail', kwargs={'pk':'2'})
#
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.put(url,{'title': u'retro',  'comment': u'second',
#                                    'project': u'http://testserver/projects/1/'}
#                               )
#
#         force_authenticate(request, user=user)
#         response = ProjectCommentDetail.as_view()(request, 2)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         ETALON = {
#              'title': u'retro', 'comment': u'second', 'id': 2,
#              'project': u'http://testserver/projects/1/', 'created_by': u'http://testserver/users/1/',
#              'created_at': u'2016-04-07T14:34:09.932000Z', 'updated_by': u'http://testserver/users/1/',
#              'updated_at': u'2016-04-08T15:45:10.387519Z', 'activity': [9,64]
#         }
#         for k in ETALON:
#             if k == 'updated_at':
#                 self.assertNotEqual(response.data[k], ETALON[k])
#             else:
#                 self.assertEqual(response.data[k], ETALON[k])
#
#     def test_project_comment_delete(self):
#         url = reverse('comments_projects:comments_detail', kwargs={'pk':'2'})
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.delete(url)
#
#         force_authenticate(request, user=user)
#         response = ProjectCommentDetail.as_view()(request, 2)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_project_comment_get(self):
#         url = reverse('comments_projects:comments_detail', kwargs={'pk':'2'})
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = ProjectCommentDetail.as_view()(request, 2)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data,
#                  {
#                         'title': u'rr', 'comment': u'second comment', 'id': 2,
#                         'project': u'http://testserver/projects/1/', 'created_by': u'http://testserver/users/1/',
#                         'created_at': u'2016-04-07T14:34:09.932000Z', 'updated_by': u'http://testserver/users/1/',
#                         'updated_at': u'2016-04-07T14:34:09.932000Z', 'activity': [9]
#                  }
#         )
#
#     def test_project_comment_delete_not_found(self):
#         url = reverse('comments_projects:comments_detail', kwargs={'pk':'10'})
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.delete(url)
#
#         force_authenticate(request, user=user)
#         response = ProjectCommentDetail.as_view()(request, 10)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#
# class TestProjectCommentFilter(APITestCase):
#     fixtures = ['project_comments.json']
#
#     def test_project_comment_filter(self):
#         url = reverse('comments_projects:comments') + '?project=1'
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = ProjectCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data['results'],
#             [
#                 {
#                     'title': u'rr', 'comment': u'second comment', 'id': 2,
#                     'project': u'http://testserver/projects/1/', 'created_by': u'http://testserver/users/1/',
#                     'created_at': u'2016-04-07T14:34:09.932000Z', 'updated_by': u'http://testserver/users/1/',
#                     'updated_at': u'2016-04-07T14:34:09.932000Z', 'activity': [9]
#                 },
#                 {
#                     'title':u'yy', 'comment': u'4', 'id': 4, 'project': u'http://testserver/projects/1/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T14:39:08.116000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T14:39:08.116000Z',
#                     'activity': [9]
#                 },
#                 {
#                     'title': u'er', 'comment': u'555', 'id': 5, 'project': u'http://testserver/projects/1/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T14:57:20.069000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T14:57:20.069000Z',
#                     'activity': [60]
#                 },
#                 {
#                     'title': u'34', 'comment': u'4444444', 'id': 6, 'project': u'http://testserver/projects/1/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T15:21:54.110000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T15:21:54.110000Z',
#                     'activity': [61]
#                 }
#             ]
#         )
#
#     def test_project_comment_filter_search(self):
#         url = reverse('comments_projects:comments') + '?search=rr'
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = ProjectCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data['results'],
#             [
#                  {
#                     'title': u'rr', 'comment': u'second comment', 'id': 2,
#                     'project': u'http://testserver/projects/1/', 'created_by': u'http://testserver/users/1/',
#                     'created_at': u'2016-04-07T14:34:09.932000Z', 'updated_by': u'http://testserver/users/1/',
#                     'updated_at': u'2016-04-07T14:34:09.932000Z', 'activity': [9]
#                  }
#             ]
#         )
#
#     def test_project_comment_filter_ordering(self):
#         url = reverse('comments_projects:comments') + '?ordering=id'
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = ProjectCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data['results'],
#             [
#                 {
#                     'title': u'rr', 'comment': u'second comment', 'id': 2,
#                     'project': u'http://testserver/projects/1/', 'created_by': u'http://testserver/users/1/',
#                     'created_at': u'2016-04-07T14:34:09.932000Z', 'updated_by': u'http://testserver/users/1/',
#                     'updated_at': u'2016-04-07T14:34:09.932000Z', 'activity': [9]
#                 },
#                 {
#                     'title':u'yy', 'comment': u'4', 'id': 4, 'project': u'http://testserver/projects/1/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T14:39:08.116000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T14:39:08.116000Z',
#                     'activity': [9]
#                 },
#                 {
#                     'title': u'er', 'comment': u'555', 'id': 5, 'project': u'http://testserver/projects/1/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T14:57:20.069000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T14:57:20.069000Z',
#                     'activity': [60]
#                 },
#                 {
#                     'title': u'34', 'comment': u'4444444', 'id': 6, 'project': u'http://testserver/projects/1/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T15:21:54.110000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T15:21:54.110000Z',
#                     'activity': [61]
#                 }
#             ]
#         )
#
#     def test_project_comment_filter_search_ordering(self):
#         url = reverse('comments_projects:comments') + '?search=r&ordering=-id'
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = ProjectCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data['results'],
#             [
#                 {
#                     'title': u'er', 'comment': u'555', 'id': 5, 'project': u'http://testserver/projects/1/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T14:57:20.069000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T14:57:20.069000Z',
#                     'activity': [60]
#                 },
#                 {
#                     'title': u'rr', 'comment': u'second comment', 'id': 2,
#                     'project': u'http://testserver/projects/1/', 'created_by': u'http://testserver/users/1/',
#                     'created_at': u'2016-04-07T14:34:09.932000Z', 'updated_by': u'http://testserver/users/1/',
#                     'updated_at': u'2016-04-07T14:34:09.932000Z', 'activity': [9]
#                 }
#             ]
#         )
#
#
# class TestTaskComment(APITestCase):
#     fixtures = ['task_comments.json']
#
#     def test_task_comment(self):
#             url = reverse('comments_tasks:comments')
#             user = get_user_model().objects.get(username='yura')
#
#             factory = APIRequestFactory()
#             request = factory.get(url)
#
#             force_authenticate(request, user=user)
#             response = TaskCommentList.as_view()(request)
#
#             self.assertEqual(response.status_code, status.HTTP_200_OK)
#             self.assertEqual(
#                 response.data['results'],
#                 [
#                     {
#                         'title': u'first', 'comment': u'1', 'id': 1, 'task': u'http://testserver/tasks/16/',
#                         'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:23:45.771000Z',
#                         'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:34:50.805000Z',
#                         'activity': [79, 81, 82]
#                     },
#                     {
#                         'title': u'second', 'comment': u'2', 'id': 2, 'task': u'http://testserver/tasks/16/',
#                         'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:26:56.484000Z',
#                         'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:26:56.484000Z',
#                         'activity': [80]
#                     },
#                     {
#                         'title': u'tema', 'comment': u'mmmm', 'id': 3, 'task': u'http://testserver/tasks/16/',
#                         'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:35:26.260000Z',
#                         'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:35:26.260000Z',
#                         'activity': [83]
#                     },
#                     {
#                         'title': u'five', 'comment': u'rest', 'id': 4, 'task': u'http://testserver/tasks/16/',
#                         'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:35:53.955000Z',
#                         'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:35:53.955000Z',
#                         'activity': [84]
#                     },
#                     {
#                         'title': u'first', 'comment': u'www', 'id': 5, 'task': u'http://testserver/tasks/15/',
#                         'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:53:44.145000Z',
#                         'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:53:44.145000Z',
#                         'activity': [85]
#                     }
#                 ]
#             )
#
#     def test_task_comment_add(self):
#         url = reverse('comments_tasks:comments')
#
#         self.client.login(username='yura', password='123')
#         response = self.client.post(url, data=
#             {
#                 'title': 'first name', 'comment': 'treee',
#                 'task': 'http://testserver/tasks/16/'
#             }
#         )
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#         ETALON = {
#             'title': u'first name', 'comment': u'treee', 'id': 6,
#             'task': u'http://testserver/tasks/16/',
#             'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-07T15:21:54.110000Z',
#             'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-07T15:21:54.110000Z',
#             'activity': [86]
#         }
#
#         for key in response.data:
#             if key in ['created_at', 'updated_at']:
#                 self.assertIsNotNone(response.data[key])
#             else:
#                 self.assertEqual(ETALON[key], response.data[key])
#
#     def test_add_task_comment_error(self):
#         url = reverse('comments_tasks:comments')
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#
#         request = factory.post(url,
#                                {'title': u'first name', 'comment': u'treee',
#                                 'task': u'http://testserver/tasks/14/'
#                                }
#         )
#
#         force_authenticate(request, user=user)
#         response = TaskCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_task_comment_not_found(self):
#         url = reverse('comments_tasks:comments_detail', kwargs={'pk': '50'})
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response =TaskCommentDetail.as_view()(request, '50')
#
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_task_comment_put(self):
#         url = reverse('comments_tasks:comments_detail', kwargs={'pk':'1'})
#
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.put(url,{'title': u'retro',  'comment': u'second',
#                                    'task': u'http://testserver/tasks/15/'}
#                               )
#
#         force_authenticate(request, user=user)
#         response = TaskCommentDetail.as_view()(request, 1)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         ETALON = {
#              'title': u'retro', 'comment': u'second', 'id': 1, 'task': u'http://testserver/tasks/15/',
#              'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:23:45.771000Z',
#              'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:34:50.805000Z',
#              'activity': [79, 81, 82, 87]
#         }
#         for k in ETALON:
#             if k == 'updated_at':
#                 self.assertNotEqual(response.data[k], ETALON[k])
#             else:
#                 self.assertEqual(response.data[k], ETALON[k])
#
#     def test_task_comment_delete(self):
#         url = reverse('comments_tasks:comments_detail', kwargs={'pk':'1'})
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.delete(url)
#
#         force_authenticate(request, user=user)
#         response = TaskCommentDetail.as_view()(request, 1)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_project_comment_get(self):
#         url = reverse('comments_tasks:comments_detail', kwargs={'pk':'1'})
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = TaskCommentDetail.as_view()(request, 1)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data,
#                  {
#                        'title': u'first', 'comment': u'1', 'id': 1, 'task': u'http://testserver/tasks/16/',
#                         'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:23:45.771000Z',
#                         'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:34:50.805000Z',
#                         'activity': [79, 81, 82]
#                  }
#         )
#
#     def test_project_comment_delete_not_found(self):
#         url = reverse('comments_tasks:comments_detail', kwargs={'pk':'20'})
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.delete(url)
#
#         force_authenticate(request, user=user)
#         response = TaskCommentDetail.as_view()(request, 20)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#
# class TestTaskCommentFilter(APITestCase):
#     fixtures = ['task_comments.json']
#
#     def test_task_comment_filter(self):
#         url = reverse('comments_tasks:comments') + '?task=15'
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = TaskCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data['results'],
#             [
#                 {
#                     'title': u'first', 'comment': u'www', 'id': 5, 'task': u'http://testserver/tasks/15/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:53:44.145000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:53:44.145000Z',
#                     'activity': [85]
#                 }
#             ]
#         )
#
#     def test_task_comment_filter_search(self):
#         url = reverse('comments_tasks:comments') + '?search=se'
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = TaskCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data['results'],
#             [
#                  {
#                     'title': u'second', 'comment': u'2', 'id': 2, 'task': u'http://testserver/tasks/16/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:26:56.484000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:26:56.484000Z',
#                     'activity': [80]
#                  }
#             ]
#         )
#
#     def test_task_comment_filter_ordering(self):
#         url = reverse('comments_tasks:comments') + '?ordering=-id'
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = TaskCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data['results'],
#             [
#                 {
#                     'title': u'first', 'comment': u'www', 'id': 5, 'task': u'http://testserver/tasks/15/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:53:44.145000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:53:44.145000Z',
#                     'activity': [85]
#                 },
#                 {
#                     'title': u'five', 'comment': u'rest', 'id': 4, 'task': u'http://testserver/tasks/16/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:35:53.955000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:35:53.955000Z',
#                     'activity': [84]
#                 },
#                 {
#                     'title': u'tema', 'comment': u'mmmm', 'id': 3, 'task': u'http://testserver/tasks/16/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:35:26.260000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:35:26.260000Z',
#                     'activity': [83]
#                 },
#                 {
#                     'title': u'second', 'comment': u'2', 'id': 2, 'task': u'http://testserver/tasks/16/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:26:56.484000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:26:56.484000Z',
#                     'activity': [80]
#                 },
#                 {
#                     'title': u'first', 'comment': u'1', 'id': 1, 'task': u'http://testserver/tasks/16/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:23:45.771000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:34:50.805000Z',
#                     'activity': [79, 81, 82]
#                 }
#             ]
#         )
#
#     def test_task_comment_filter_search_ordering(self):
#         url = reverse('comments_tasks:comments') + '?search=fi&ordering=-id'
#         user = get_user_model().objects.get(username='yura')
#
#         factory = APIRequestFactory()
#         request = factory.get(url)
#
#         force_authenticate(request, user=user)
#         response = TaskCommentList.as_view()(request)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(
#             response.data['results'],
#             [
#                 {
#                     'title': u'first', 'comment': u'www', 'id': 5, 'task': u'http://testserver/tasks/15/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:53:44.145000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:53:44.145000Z',
#                     'activity': [85]
#                 },
#                 {
#                     'title': u'five', 'comment': u'rest', 'id': 4, 'task': u'http://testserver/tasks/16/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:35:53.955000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:35:53.955000Z',
#                     'activity': [84]
#                 },
#                 {
#                     'title': u'first', 'comment': u'1', 'id': 1, 'task': u'http://testserver/tasks/16/',
#                     'created_by': u'http://testserver/users/1/', 'created_at': u'2016-04-11T11:23:45.771000Z',
#                     'updated_by': u'http://testserver/users/1/', 'updated_at': u'2016-04-11T11:34:50.805000Z',
#                     'activity': [79, 81, 82]
#                 }
#             ]
#         )
