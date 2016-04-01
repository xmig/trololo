from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
import json
from projects.models import Project, Task


class TestProjectTags(APITestCase):
    fixtures = ["tags_data.json"]

    def tearDown(self):
        self.client.logout()

    def test_set_project_tags(self):
        self.client.login(username='cartman', password='123')

        url = reverse("projects:projects_detail", kwargs={"pk": 3})

        response = self.client.put(
            url, {"tags": [{"name": "backend"}, {"name": "production"}]}, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_proj_data = {
            "name": "projectc",
            "id": 3,
            "description": "aaa",
            "status": "undefined",
            "members": [],
            "comments": [],
            "visible_by": "undefined",
            "tasks": [
                "http://testserver/tasks/3/"
            ],
            "date_started": "2016-03-03T10:57:11Z",
            "date_finished": None,
            "created_by": "http://testserver/users/11/",
            "created_at": "2016-03-02T10:56:37Z",
            "updated_by": "http://testserver/users/11/",
            "updated_at": "2016-03-02T10:56:37Z",
            "tags": [
                {"name": "backend"}, {"name": "production"}
            ]
        }

        content = json.loads(response.content)

        for k, v in content.iteritems():
            if k != "updated_at":
                self.assertEqual(v, new_proj_data[k])
            else:
                self.assertNotEqual(v, new_proj_data[k])

        pr3 = Project.objects.get(pk=3)

        self.assertEqual(
            set(pr3.tags.names()), set(["backend", "production"])
        )

    def test_update_project_tags(self):
        self.client.login(username='yura', password='123')

        url = reverse("projects:projects_detail", kwargs={"pk": 1})
        response = self.client.put(
            url, {"tags": [{"name": "chi software"}, {"name": "stage"}]}, format='json'
        )

        new_proj_data = {
            "id": 1,
            "status": "undefined",
            "name": "projecta",
            "date_finished": None,
            "created_at": "2016-03-02T10:56:37Z",
            "description": "eee",
            "visible_by": "undefined",
            "updated_at": "2016-03-31T13:06:54.869Z",
            "created_by": "http://testserver/users/1/",
            "comments": [],
            "members": [
                "http://testserver/users/1/",
                "http://testserver/users/11/"
            ],
            "date_started": "2016-03-01T10:56:19Z",
            "updated_by": "http://testserver/users/1/",
            "tags": [{"name": "chi software"}, {"name": "stage"}],
            "tasks": [
                "http://testserver/tasks/1/",
                "http://testserver/tasks/2/"
            ]
        }
        content = json.loads(response.content)

        for k, v in content.iteritems():
            if k != "updated_at":
                self.assertEqual(v, new_proj_data[k], "{}: {} != {}".format(k, v, new_proj_data[k]))
            else:
                self.assertNotEqual(v, new_proj_data[k], "{}: {} == {}".format(k, v, new_proj_data[k]))

        pr1 = Project.objects.get(pk=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(pr1.tags.names()), set(["chi software", "stage"])
        )

    def test_get_filter_project_by_tags(self):
        self.client.login(username='yura', password='123')

        url = reverse("projects:projects") + '?tag=chi%20software'

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        new_proj_data = {
            "id": 1,
            "status": "undefined",
            "name": "projecta",
            "date_finished": None,
            "created_at": "2016-03-02T10:56:37Z",
            "description": "eee",
            "visible_by": "undefined",
            "updated_at": "2016-03-31T13:06:54.869000Z",
            "created_by": "http://testserver/users/1/",
            "comments": [],
            "members": [
                "http://testserver/users/1/",
                "http://testserver/users/11/"
            ],
            "date_started": "2016-03-01T10:56:19Z",
            "updated_by": "http://testserver/users/11/",
            "tags": [{"name": "chi software"}],
            "tasks": [
                "http://testserver/tasks/1/",
                "http://testserver/tasks/2/"
            ]
        }
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content["count"], 1)

        for k, v in content["results"][0].iteritems():
            self.assertEqual(v, new_proj_data[k], "{}: {} != {}".format(k, v, new_proj_data[k]))

    def test_get_filter_project_by_absent_tag(self):
        self.client.login(username='yura', password='123')

        url = reverse("projects:projects") + '?tag=chi'

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content["count"], 0)

        self.assertEqual(content["results"], [])


class TestTaskTags(APITestCase):
    fixtures = ["tags_data.json"]

    def setUp(self):
        self.client.login(username='yura', password='123')

    def tearDown(self):
        self.client.logout()

    def test_set_task_tags(self):
        url = reverse("tasks:tasks_detail", kwargs={"pk": 1})

        response = self.client.put(
            url, {"tags": [{"name": "user"}, {"name": "production"}]}, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        new_task_data = {
            "name": "task1",
            "id": 1,
            "description": "",
            "status": "undefined",
            "members": [],
            "type": "undefined",
            "label": "undefined",
            "project": "http://testserver/projects/1/",
            "comments": [],
            "deadline_date": "2016-03-06T10:57:47Z",
            "estimate_minutes": None,
            "created_by": "http://testserver/users/11/",
            "created_at": "2016-03-18T10:57:49.589000Z",
            "updated_by": "http://testserver/users/1/",
            "updated_at": "2016-03-31T13:06:54.610027Z",
            "tags": [{"name": "production"}, {"name": "user"}]
        }

        content = json.loads(response.content)

        for k, v in content.iteritems():
            if k != "updated_at":
                self.assertEqual(v, new_task_data[k])
            else:
                self.assertNotEqual(v, new_task_data[k])

        task3 = Task.objects.get(pk=1)

        self.assertEqual(
            set(task3.tags.names()), set(["user", "production"])
        )

    def test_get_filter_task_by_tags(self):
        url = reverse("tasks:tasks") + '?tag=cisco'

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        task_data = {
            "name": "task1",
            "id": 1,
            "description": "",
            "status": "undefined",
            "members": [],
            "type": "undefined",
            "label": "undefined",
            "project": "http://testserver/projects/1/",
            "comments": [],
            "deadline_date": "2016-03-06T10:57:47Z",
            "estimate_minutes": None,
            "created_by": "http://testserver/users/11/",
            "created_at": "2016-03-18T10:57:49.589000Z",
            "updated_by": "http://testserver/users/11/",
            "updated_at": "2016-03-31T13:06:54.610000Z",
            "tags": [{"name": "cisco"}]
        }
        content = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content["count"], 1)

        for k, v in content["results"][0].iteritems():
            self.assertEqual(v, task_data[k], "{}: {} != {}".format(k, v, task_data[k]))