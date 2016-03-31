from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.contrib.auth import get_user_model
from projects.views import ProjectsList, TaskList
from rest_framework.reverse import reverse
from rest_framework import status
from projects.views import ProjectDetail, TaskDetail


class TestProjectFilter(APITestCase):
    fixtures = ['all_data.json']

    def test_get_project_filter(self):
        url = reverse('projects:projects')
        user = get_user_model().objects.get(username='admin')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = ProjectsList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = [
            {
                "name": u"project_01", u"id": 1, "description": u"some_project_description",
                "status": u"breakthrough","members": [u'http://testserver/users/1/'],
                "visible_by": u"particular_user",
                "tasks": [u'http://testserver/tasks/2/', u'http://testserver/tasks/1/'], "comments": [],"date_started": "2016-01-01T14:32:00Z",
                "date_finished": "2016-03-03T14:02:00Z", "created_by": u'http://testserver/users/1/',
                "created_at": u"2016-03-24T10:36:51.551000Z", "updated_by": u'http://testserver/users/1/',
                "updated_at": u"2016-03-24T11:03:40.020000Z"
            },
            {
                "name": u"project_02", u"id": 2, "description": u"some_project_02_description",
                "status": u"breakthrough","members": [u'http://testserver/users/1/'],
                "visible_by": u"particular_user",
                "tasks": [], "comments": [],"date_started": u"2016-01-01T14:32:00Z",
                "date_finished": u"2016-03-03T14:02:00Z", "created_by": u'http://testserver/users/1/',
                "created_at": u"2016-03-24T10:36:51.551000Z", "updated_by": u'http://testserver/users/1/',
                "updated_at": u"2016-03-24T11:03:40.020000Z"
            }
        ]
        for i, d in enumerate(response.data['results']):
            for k, v in d.iteritems():
                self.assertEqual(v, results[i][k])


class TestProjectFilterList(APITestCase):
    fixtures = ['data_with_gravatar.json']

    def test_project_filter(self):
        url = reverse('projects:projects') + '?name=projecta'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = ProjectsList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'http://testserver/users/1/'], 'visible_by': u'undefined',
                    'tasks': [u'http://testserver/tasks/2/', u'http://testserver/tasks/1/'],
                    'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
                    'date_finished': None, 'created_by': None,
                    'created_at': u'2016-03-02T10:56:37Z', 'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'
                },
                {
                    'name': u'projecta', 'id': 4, 'description': u'aa', 'status': u'undefined', 'members': [],
                    'visible_by': u'undefined','tasks': [], 'comments': [], 'date_started': u'2016-03-30T14:17:49Z',
                    'date_finished': None, 'created_by': None,'created_at': u'2016-03-02T10:56:37Z',
                    'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'

                }
            ]
        )

    def test_project_filter_second(self):
        url = reverse('projects:projects') + '?name=projecta&description=eee'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = ProjectsList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'http://testserver/users/1/'], 'visible_by': u'undefined',
                    'tasks': [u'http://testserver/tasks/2/', u'http://testserver/tasks/1/'],
                    'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
                    'date_finished': None, 'created_by': None,
                    'created_at': u'2016-03-02T10:56:37Z', 'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'
                }
            ]
        )

    def test_project_filter_search(self):
        url = reverse('projects:projects') + '?search=projecta'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = ProjectsList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'http://testserver/users/1/'], 'visible_by': u'undefined',
                    'tasks': [u'http://testserver/tasks/2/', u'http://testserver/tasks/1/'],
                    'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
                    'date_finished': None, 'created_by': None,
                    'created_at': u'2016-03-02T10:56:37Z', 'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'
                },
                {
                    'name': u'projecta', 'id': 4, 'description': u'aa', 'status': u'undefined', 'members': [],
                    'visible_by': u'undefined','tasks': [], 'comments': [], 'date_started': u'2016-03-30T14:17:49Z',
                    'date_finished': None, 'created_by': None,'created_at': u'2016-03-02T10:56:37Z',
                    'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'

                }
            ]
        )

    def test_project_filter_ordering_search(self):
        url = reverse('projects:projects') + '?search=projecta&ordering=visible_by,-id'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = ProjectsList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    'name': u'projecta', 'id': 4, 'description': u'aa', 'status': u'undefined', 'members': [],
                    'visible_by': u'undefined','tasks': [], 'comments': [], 'date_started': u'2016-03-30T14:17:49Z',
                    'date_finished': None, 'created_by': None,'created_at': u'2016-03-02T10:56:37Z',
                    'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'
                },
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'http://testserver/users/1/'], 'visible_by': u'undefined',
                    'tasks': [u'http://testserver/tasks/2/', u'http://testserver/tasks/1/'],
                    'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
                    'date_finished': None, 'created_by': None,
                    'created_at': u'2016-03-02T10:56:37Z', 'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'
                },
            ]
        )

    def test_project_filter_ordering(self):
        url = reverse('projects:projects') + '?ordering=-id'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = ProjectsList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    'name': u'projecta', 'id': 4, 'description': u'aa', 'status': u'undefined', 'members': [],
                    'visible_by': u'undefined','tasks': [], 'comments': [], 'date_started': u'2016-03-30T14:17:49Z',
                    'date_finished': None, 'created_by': None,'created_at': u'2016-03-02T10:56:37Z',
                    'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'
                },
                {
                    "name": u"projectc", u"id": 3, "description": u"aaa", "status": u"undefined",
                    "members": [], "visible_by": u"undefined", "tasks": [u'http://testserver/tasks/3/'],
                    "comments": [], "date_started": u"2016-03-03T10:57:11Z", "date_finished": None, "created_by": None,
                    "created_at": u"2016-03-02T10:56:37Z", "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"projectb", u"id": 2, "description": u"bbbb", "status": u"undefined",
                    "members": [u'http://testserver/users/2/'], "visible_by": u"undefined",
                    "tasks": [u'http://testserver/tasks/5/', u'http://testserver/tasks/4/'],
                    "comments": [], "date_started": u"2016-03-02T10:56:37Z", "date_finished": None,
                    "created_by": None, "created_at": "2016-03-02T10:56:37Z", "updated_by": None,
                    "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'http://testserver/users/1/'], 'visible_by': u'undefined',
                    'tasks': [u'http://testserver/tasks/2/', u'http://testserver/tasks/1/'],
                    'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
                    'date_finished': None, 'created_by': None,
                    'created_at': u'2016-03-02T10:56:37Z', 'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'
                }
            ]
        )


class TestProjectTaskFilter(APITestCase):
    fixtures = ['data_with_gravatar.json']

    def test_task_filter(self):
        url = reverse('tasks:tasks') + '?name=task1'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = TaskList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    "name": u"task1", "id": 1, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/1/",
                    "comments": [], "deadline_date": u"2016-03-06T10:57:47Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T10:57:49.589000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                }
            ]
        )

    def test_task_filter_search(self):
        url = reverse('tasks:tasks') + '?search=task5'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = TaskList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    "name": u"task5", "id": 5, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/2/",
                    "comments": [], "deadline_date": u"2016-03-31T11:11:22Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T11:10:21.110000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                }
            ]
        )

    def test_task_filter_ordering(self):
        url = reverse('tasks:tasks') + '?ordering=-name'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = TaskList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    "name": u"task5", "id": 5, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/2/",
                    "comments": [], "deadline_date": u"2016-03-31T11:11:22Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T11:10:21.110000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"task4", "id": 4, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/2/",
                    "comments": [], "deadline_date": u"2016-03-23T11:07:17Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T11:07:19.325000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"task3", "id": 3, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/3/",
                    "comments": [], "deadline_date": u"2016-03-07T10:59:12Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T10:59:14.494000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"task2", "id": 2, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/1/",
                    "comments": [], "deadline_date": u"2016-03-07T10:58:29Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T10:58:31.790000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"task1", "id": 1, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/1/",
                    "comments": [], "deadline_date": u"2016-03-06T10:57:47Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T10:57:49.589000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                }
            ]
        )



class TestProjectDetailGet(APITestCase):
    fixtures = ['all_data.json']

    def test_get_project(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        ETALON = {
                "status": u'breakthrough', "name": u'project_01', "date_finished": u"2016-03-03T14:02:00Z", "created_at": u'2016-03-24T10:36:51.551000Z',
                "description": u'some_project_description', "visible_by": u'particular_user', "updated_at": u'2016-03-24T11:03:40.020000Z',
                "created_by": u'http://testserver/users/1/', "members": [u'http://testserver/users/1/'],
                "activity": [1, 4],
                "date_started": u"2016-01-01T14:32:00Z",
                "updated_by": u'http://testserver/users/1/', "id": 1
            }

        for k in ETALON:
            if k in response.data:
                self.assertEqual(response.data[k], ETALON[k])



class TestProjectUpdate(APITestCase):
    fixtures = ['all_data.json']

    def test_project_name_update(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'name': 'test_project'})

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "name": u'test_project', "date_finished": u"2016-03-03T14:02:00Z", "created_at": u'2016-03-24T10:36:51.551000Z',
                "description": u'some_project_description', "visible_by": u'particular_user', "updated_at": u'2016-03-24T11:03:40.020000Z',
                "created_by": u'http://testserver/users/1/', "members": [u'http://testserver/users/1/'],
                "date_started": u"2016-01-01T14:32:00Z", "updated_by": u'http://testserver/users/1/', "id": 1
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])



    def test_project_members_update(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'members': [u'http://testserver/users/1/', u'http://testserver/users/2/']})

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "name": u'project_01', "date_finished": u"2016-03-03T14:02:00Z", "created_at": u'2016-03-24T10:36:51.551000Z',
                "description": u'some_project_description', "visible_by": u'particular_user', "updated_at": u'2016-03-24T11:03:40.020000Z',
                "created_by": u'http://testserver/users/1/', "members": [u'http://testserver/users/1/', u'http://testserver/users/2/'],
                "date_started": u"2016-01-01T14:32:00Z", "updated_by": u'http://testserver/users/1/', "id": 1
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_project_status_update(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'status': 'finished'})

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'finished', "name": u'project_01', "date_finished": u"2016-03-03T14:02:00Z", "created_at": u'2016-03-24T10:36:51.551000Z',
                "description": u'some_project_description', "visible_by": u'particular_user', "updated_at": u'2016-03-24T11:03:40.020000Z',
                "created_by": u'http://testserver/users/1/', "members": [u'http://testserver/users/1/'],
                "date_started": u"2016-01-01T14:32:00Z", "updated_by": u'http://testserver/users/1/', "id": 1
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_project_description_update(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'description': 'new_description'})

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "name": u'project_01', "date_finished": "2016-03-03T14:02:00Z", "created_at": u'2016-03-24T10:36:51.551000Z',
                "description": u'new_description', "visible_by": u'particular_user', "updated_at": u'2016-03-24T11:03:40.020000Z',
                "created_by": u'http://testserver/users/1/', "members": [u'http://testserver/users/1/'],
                "date_started": u"2016-01-01T14:32:00Z", "updated_by": u'http://testserver/users/1/', "id": 1
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_project_visible_by_update(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'visible_by': 'all_users'})

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "name": u'project_01', "date_finished": "2016-03-03T14:02:00Z", "created_at": u'2016-03-24T10:36:51.551000Z',
                "description": u'some_project_description', "visible_by": u'all_users', "updated_at": u'2016-03-24T11:03:40.020000Z',
                "created_by": u'http://testserver/users/1/', "members": [u'http://testserver/users/1/'],
                "date_started": u"2016-01-01T14:32:00Z", "updated_by": u'http://testserver/users/1/', "id": 1
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_project_date_started_update(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'date_started': u"2016-02-01T14:32:00Z"})

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "name": u'project_01', "date_finished": u"2016-03-03T14:02:00Z", "created_at": u'2016-03-24T10:36:51.551000Z',
                "description": u'some_project_description', "visible_by": u'particular_user', "updated_at": u'2016-03-24T11:03:40.020000Z',
                "created_by": u'http://testserver/users/1/', "members": [u'http://testserver/users/1/'],
                "date_started": u"2016-02-01T14:32:00Z", "updated_by": u'http://testserver/users/1/', "id": 1
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_project_date_finished_update(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'date_finished': u"2016-03-03T14:02:00Z"})

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "name": u'project_01', "date_finished": u"2016-03-03T14:02:00Z", "created_at": u'2016-03-24T10:36:51.551000Z',
                "description": u'some_project_description', "visible_by": u'particular_user', "updated_at": u'2016-03-24T11:03:40.020000Z',
                "created_by": u'http://testserver/users/1/', "members": [u'http://testserver/users/1/'],
                "date_started": u"2016-01-01T14:32:00Z", "updated_by": u'http://testserver/users/1/', "id": 1
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_project_tasks_update(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory = APIRequestFactory()
        request = factory.put(url, {'tasks': [u'http://testserver/tasks/2/']})

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)


        ETALON = {
                "status": u'breakthrough', "name": u'project_01', "date_finished": u"2016-03-03T14:02:00Z", "created_at": u'2016-03-24T10:36:51.551000Z',
                "description": u'some_project_description', "visible_by": u'particular_user', "updated_at": u'2016-03-24T11:03:40.020000Z',
                "created_by": u'http://testserver/users/1/', "members": [u'http://testserver/users/1/'],
                "date_started": u"2016-01-01T14:32:00Z", "updated_by": u'http://testserver/users/1/', "id": 1,
                'tasks': [u'http://testserver/tasks/2/']
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])



class TestProjectDelete(APITestCase):
    fixtures = ['all_data.json']

    def test_task_name_update(self):
        url = reverse('projects:projects_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.delete(url)

        force_authenticate(request, user=user)
        response = ProjectDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        ETALON = {}

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])



class TestTaskDetailGet(APITestCase):
    fixtures = ['all_data.json']

    def test_get_task(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        ETALON = {
                "status": u'breakthrough', "estimate_minutes": 5, "name": u'task_01', "created_at": u'2016-03-24T11:00:11.106000Z',
                "updated_at": u'2016-03-28T07:27:10.444039Z', "updated_by": u'http://testserver/users/1/', "label": u'red',
                "project": u'http://testserver/projects/1/', "deadline_date": None, "created_by": u'http://testserver/users/1/',
                "members": [u'http://testserver/users/1/'], "type": u'bug', "description": u'task_01_description'
            }

        for k in ETALON:
            if k in response.data:
                self.assertEqual(response.data[k], ETALON[k])



class TestTaskUpdate(APITestCase):
    fixtures = ['all_data.json']

    def test_task_name_update(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'name': 'task_01_new'})

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
            "status": "breakthrough", "estimate_minutes": 5, "name": "task_01_new", "created_at": "2016-03-24T11:00:11.106000Z",
            "updated_at": "2016-03-28T07:27:10.444039Z", "updated_by": u'http://testserver/users/1/', "label": "red",
            "project": u'http://testserver/projects/1/', "deadline_date": None, "created_by": u'http://testserver/users/1/',
            "members": [u'http://testserver/users/1/'], "type": "bug", "description": "task_01_description"
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])



    def test_task_description_update(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'description': u'task_01_description_new'})

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "estimate_minutes": 5, "name": u'task_01', "created_at": u'2016-03-24T11:00:11.106000Z',
                "updated_at": u'2016-03-28T07:27:10.444039Z', "updated_by": u'http://testserver/users/1/', "label": u'red',
                "project": u'http://testserver/projects/1/', "deadline_date": None, "created_by": u'http://testserver/users/1/',
                "members": [u'http://testserver/users/1/'], "type": u'bug', "description": u'task_01_description_new'
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])



    def test_task_project_update(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'project': u'http://testserver/projects/2/'})

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "estimate_minutes": 5, "name": u'task_01', "created_at": u'2016-03-24T11:00:11.106000Z',
                "updated_at": u'2016-03-28T07:27:10.444039Z', "updated_by": u'http://testserver/users/1/', "label": u'red',
                "project": u'http://testserver/projects/2/', "deadline_date": None, "created_by": u'http://testserver/users/1/',
                "members": [u'http://testserver/users/1/'], "type": u'bug', "description": u'task_01_description'
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_task_members_update(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'members': [u'http://testserver/users/2/']})

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "estimate_minutes": 5, "name": u'task_01', "created_at": u'2016-03-24T11:00:11.106000Z',
                "updated_at": u'2016-03-28T07:27:10.444039Z', "updated_by": u'http://testserver/users/1/', "label": u'red',
                "project": u'http://testserver/projects/1/', "deadline_date": None, "created_by": u'http://testserver/users/1/',
                "members": [u'http://testserver/users/2/'], "type": u'bug', "description": u'task_01_description'
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_task_status_update(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'status': 'finished'})

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'finished', "estimate_minutes": 5, "name": u'task_01', "created_at": u'2016-03-24T11:00:11.106000Z',
                "updated_at": u'2016-03-28T07:27:10.444039Z', "updated_by": u'http://testserver/users/1/', "label": u'red',
                "project": u'http://testserver/projects/1/', "deadline_date": None, "created_by": u'http://testserver/users/1/',
                "members": [u'http://testserver/users/1/'], "type": u'bug', "description": u'task_01_description'
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_task_type_update(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'type': 'feature'})

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "estimate_minutes": 5, "name": u'task_01', "created_at": u'2016-03-24T11:00:11.106000Z',
                "updated_at": u'2016-03-24T11:00:11.106000Z', "updated_by": u'http://testserver/users/1/', "label": u'red',
                "project": u'http://testserver/projects/1/', "deadline_date": None, "created_by": u'http://testserver/users/1/',
                "members": [u'http://testserver/users/1/'], "type": u'feature', "description": u'task_01_description'
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_task_label(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'label': u"green"})

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "estimate_minutes": 5, "name": u'task_01', "created_at": u'2016-03-24T11:00:11.106000Z',
                "updated_at": u'2016-03-24T11:00:11.106000Z', "updated_by": u'http://testserver/users/1/', "label": u'green',
                "project": u'http://testserver/projects/1/', "deadline_date": None, "created_by": u'http://testserver/users/1/',
                "members": [u'http://testserver/users/1/'], "type": u'bug', "description": u'task_01_description'
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_deadline_date(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'deadline_date': u'2016-05-24T11:00:11.106000Z'})

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "estimate_minutes": 5, "name": u'task_01', "created_at": u'2016-03-24T11:00:11.106000Z',
                "updated_at": u'2016-03-24T11:00:11.106000Z', "updated_by": u'http://testserver/users/1/', "label": u'red',
                "project": u'http://testserver/projects/1/', "deadline_date": u'2016-05-24T11:00:11.106000Z', "created_by": u'http://testserver/users/1/',
                "members": [u'http://testserver/users/1/'], "type": u'bug', "description": u'task_01_description'
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])


    def test_task_estimate(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.put(url, {'estimate_minutes': 7})

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        ETALON = {
                "status": u'breakthrough', "estimate_minutes": 7, "name": u'task_01', "created_at": u'2016-03-24T11:00:11.106000Z',
                "updated_at": u'2016-03-24T11:00:11.106000Z', "updated_by": u'http://testserver/users/1/', "label": u'red',
                "project": u'http://testserver/projects/1/', "deadline_date": None, "created_by": u'http://testserver/users/1/',
                "members": [u'http://testserver/users/1/'], "type": u'bug', "description": u'task_01_description'
            }

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])




class TestTaskDelete(APITestCase):
    fixtures = ['all_data.json']

    def test_task_name_update(self):
        url = reverse('tasks:tasks_detail', kwargs={'pk': '1'})
        user = get_user_model().objects.get(username='admin')

        factory =APIRequestFactory()
        request = factory.delete(url)

        force_authenticate(request, user=user)
        response = TaskDetail.as_view()(request, '1')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        ETALON = {}

        for k in ETALON:
            if k == 'updated_at':
                self.assertNotEqual(response.data[k], ETALON[k])
            else:
                self.assertEqual(response.data[k], ETALON[k])