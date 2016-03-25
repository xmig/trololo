from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.contrib.auth import get_user_model
from projects.views import ProjectsList
from rest_framework.reverse import reverse


class TestProjectFilter(APITestCase):
    fixtures = ['all_data.json']

    def test_get_project_filter(self):
        url = reverse('projects:projects')
        user = get_user_model().objects.get(username='admin')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        responce = ProjectsList.as_view()(request)

        self.assertEqual(
            responce.data['results'],
            [
                {
                    "name": u"project_01", u"id": 1, "description": u"some_project_description",
                    "status": u"breakthrough","members": [u'admin'], "visible_by": u"particular_user",
                    "tasks": [u"task_01"], "comments": [],"date_started": None, "date_finished": None, "created_by":1,
                    "created_at": u"2016-03-24T10:36:51.551000Z", "updated_by": 1,
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
        responce = ProjectsList.as_view()(request)

        self.assertEqual(
            responce.data['results'],
            [
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'yura'], 'visible_by': u'undefined',
                    'tasks': [u'task2', u'task1'], 'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
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
        responce = ProjectsList.as_view()(request)

        self.assertEqual(
            responce.data['results'],
            [
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'yura'], 'visible_by': u'undefined',
                    'tasks': [u'task2', u'task1'], 'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
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
        responce = ProjectsList.as_view()(request)

        self.assertEqual(
            responce.data['results'],
            [
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'yura'], 'visible_by': u'undefined',
                    'tasks': [u'task2', u'task1'], 'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
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
        responce = ProjectsList.as_view()(request)

        self.assertEqual(
            responce.data['results'],
            [
                {
                    'name': u'projecta', 'id': 4, 'description': u'aa', 'status': u'undefined', 'members': [],
                    'visible_by': u'undefined','tasks': [], 'comments': [], 'date_started': u'2016-03-30T14:17:49Z',
                    'date_finished': None, 'created_by': None,'created_at': u'2016-03-02T10:56:37Z',
                    'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'

                },
                {
                    'name': u'projecta', 'id': 1, 'description': u'eee', 'status': u'undefined',
                    'members': [u'yura'], 'visible_by': u'undefined',
                    'tasks': [u'task2', u'task1'], 'comments': [], 'date_started': u'2016-03-01T10:56:19Z',
                    'date_finished': None, 'created_by': None,
                    'created_at': u'2016-03-02T10:56:37Z', 'updated_by': None, 'updated_at': u'2016-03-02T10:56:37Z'
                }
            ]
        )

    def test_project_filter_ordering(self):
        url = reverse('projects:projects') + '?ordering=-id'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        responce = ProjectsList.as_view()(request)

        self.assertEqual(
            responce.data['results'],
            [
                {
                    "name": u"projecta", u"id": 4, "description": u"aa", "status": u"undefined", "members": [],
                    "visible_by": u"undefined", "tasks": [], "comments": [], "date_started": u"2016-03-30T14:17:49Z",
                    "date_finished": None,"created_by": None, "created_at": u"2016-03-02T10:56:37Z",
                    "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"projectc", u"id": 3, "description": u"aaa", "status": u"undefined",
                    "members": [], "visible_by": u"undefined", "tasks": [u"task3"],
                    "comments": [], "date_started": u"2016-03-03T10:57:11Z", "date_finished": None, "created_by": None,
                    "created_at": u"2016-03-02T10:56:37Z", "updated_by": None, "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"projectb", u"id": 2, "description": u"bbbb", "status": u"undefined",
                    "members": [u"yura2"], "visible_by": u"undefined", "tasks": [u"task5",u"task4"],
                    "comments": [], "date_started": u"2016-03-02T10:56:37Z", "date_finished": None,
                    "created_by": None, "created_at": "2016-03-02T10:56:37Z", "updated_by": None,
                    "updated_at": u"2016-03-02T10:56:37Z"
                },
                {
                    "name": u"projecta", u"id": 1, "description": u"eee", "status": u"undefined", "members": [u"yura"],
                    "visible_by": u"undefined", "tasks": [u"task2", u"task1"], "comments": [],
                    "date_started": u"2016-03-01T10:56:19Z", "date_finished": None, "created_by": None,
                    "created_at": u"2016-03-02T10:56:37Z", "updated_by": None,
                    "updated_at": u"2016-03-02T10:56:37Z"
                }
            ]
        )

