from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.contrib.auth import get_user_model
from projects.views import ProjectsList, TaskList
from rest_framework.reverse import reverse
from rest_framework import status

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
        self.assertEqual(
            response.data['results'],
            [
                {
                    "name": u"project_01", u"id": 1, "description": u"some_project_description",
                    "status": u"breakthrough","members": [u'http://testserver/users/1/'],
                    "visible_by": u"particular_user",
                    "tasks": [u"http://testserver/projects/tasks/1/"], "comments": [],"date_started": None,
                    "date_finished": None, "created_by": u'http://testserver/users/1/',
                    "created_at": u"2016-03-24T10:36:51.551000Z", "updated_by": u'http://testserver/users/1/',
                    "updated_at": u"2016-03-24T11:03:40.020000Z"
                }
            ]
        )


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
                    'tasks': [u'http://testserver/projects/tasks/2/', u'http://testserver/projects/tasks/1/'],
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
                    'tasks': [u'http://testserver/projects/tasks/2/', u'http://testserver/projects/tasks/1/'],
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
                    'tasks': [u'http://testserver/projects/tasks/2/', u'http://testserver/projects/tasks/1/'],
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
                    'tasks': [u'http://testserver/projects/tasks/2/', u'http://testserver/projects/tasks/1/'],
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
                    "members": [], "visible_by": u"undefined", "tasks": [u'http://testserver/projects/tasks/3/'],
                    "comments": [], "date_started": u"2016-03-03T10:57:11Z", "date_finished": None, "created_by": None,
                    "created_at": u"2016-03-02T10:56:37Z", "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"projectb", u"id": 2, "description": u"bbbb", "status": u"undefined",
                    "members": [u'http://testserver/users/2/'], "visible_by": u"undefined",
                    "tasks": [u'http://testserver/projects/tasks/5/', u'http://testserver/projects/tasks/4/'],
                    "comments": [], "date_started": u"2016-03-02T10:56:37Z", "date_finished": None,
                    "created_by": None, "created_at": "2016-03-02T10:56:37Z", "updated_by": None,
                    "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'http://testserver/users/1/'], 'visible_by': u'undefined',
                    'tasks': [u'http://testserver/projects/tasks/2/', u'http://testserver/projects/tasks/1/'],
                    'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
                    'date_finished': None, 'created_by': None,
                    'created_at': u'2016-03-02T10:56:37Z', 'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'
                }
            ]
        )


class TestProjectTaskFilter(APITestCase):
    fixtures = ['data_with_gravatar.json']

    def test_task_filter(self):
        url = reverse('projects:projects') + '?name=task1'
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
                    "project": u"http://testserver/projects/projects/1/",
                    "comments": [], "deadline_date": u"2016-03-06T10:57:47Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T10:57:49.589000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                }
            ]
        )

    def test_task_filter_search(self):
        url = reverse('projects:projects') + '?search=task5'
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
                    "project": u"http://testserver/projects/projects/2/",
                    "comments": [], "deadline_date": u"2016-03-31T11:11:22Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T11:10:21.110000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                }
            ]
        )

    def test_task_filter_ordering(self):
        url = reverse('projects:projects') + '?ordering=-name'
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
                    "project": u"http://testserver/projects/projects/2/",
                    "comments": [], "deadline_date": u"2016-03-31T11:11:22Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T11:10:21.110000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"task4", "id": 4, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/projects/2/",
                    "comments": [], "deadline_date": u"2016-03-23T11:07:17Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T11:07:19.325000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"task3", "id": 3, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/projects/3/",
                    "comments": [], "deadline_date": u"2016-03-07T10:59:12Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T10:59:14.494000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"task2", "id": 2, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/projects/1/",
                    "comments": [], "deadline_date": u"2016-03-07T10:58:29Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T10:58:31.790000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"task1", "id": 1, "description": u"", "status": u"undefined",
                    "members": [], "type": u"undefined", "label": u"undefined",
                    "project": u"http://testserver/projects/projects/1/",
                    "comments": [], "deadline_date": u"2016-03-06T10:57:47Z", "estimate_minutes": None,
                    "created_by": None, "created_at": u"2016-03-18T10:57:49.589000Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                }
            ]
        )