from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.contrib.auth import get_user_model
from projects.views_status import StatusView, StatusDetail
from rest_framework.reverse import reverse
from rest_framework import status

class TestStatus(APITestCase):
    fixtures = ['data_with_gravatar.json']

    def test_status(self):
            url = reverse('statuses:status')
            user = get_user_model().objects.get(username='yura')

            factory = APIRequestFactory()
            request = factory.get(url)

            force_authenticate(request, user=user)
            response = StatusView.as_view()(request)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(
                response.data['results'],
                [
                    {
                        'name':u'inprogress', 'order_number': 1, 'url':  u'http://testserver/status/status/1/',
                        'project': u'http://testserver/projects/1/'
                    },
                    {
                        'name':u'done', 'order_number': 2, 'url':  u'http://testserver/status/status/2/',
                        'project': u'http://testserver/projects/1/'
                    },
                    {
                        'name':u'inprogress1', 'order_number': 1, 'url':  u'http://testserver/status/status/3/',
                        'project': u'http://testserver/projects/2/'
                    },
                    {
                        'name': u'done', 'order_number': 2, 'url': u'http://testserver/status/status/4/',
                        'project': u'http://testserver/projects/2/'
                    }
                ]
            )

    def test_add_status(self):
        url = reverse('statuses:status')
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()

        request = factory.post(url, {'name': 'first name', 'order_number': 1,
                                    'project': 'http://testserver/projects/1/'}
                              )

        force_authenticate(request, user=user)
        response = StatusView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data,
                 {
                    'name': u'first name', 'order_number': 1, 'url':  u'http://testserver/status/status/5/',
                    'project': u'http://testserver/projects/1/'
                 }
        )

    def test_add_status_error(self):
        url = reverse('statuses:status')
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()

        request = factory.post(url, {'name': 'first name', 'order_number': 1})

        force_authenticate(request, user=user)
        response = StatusView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_status_not_found(self):
        url = reverse('statuses:status_detail', kwargs={'pk': '10'})
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response =StatusDetail.as_view()(request, '10')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_put(self):
        url = reverse('statuses:status_detail', kwargs={'pk':'1'})
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.put(url,{'name': 'in', 'order_number': 1,
                                    'project': 'http://testserver/projects/1/'}
                              )

        force_authenticate(request, user=user)
        response = StatusDetail.as_view()(request, 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
                 {
                    'name': u'in', 'order_number': 1, 'url':  u'http://testserver/status/status/1/',
                    'project': u'http://testserver/projects/1/'
                 }
        )

    def test_status_delete(self):
        url = reverse('statuses:status_detail', kwargs={'pk':'1'})
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.delete(url)

        force_authenticate(request, user=user)
        response = StatusDetail.as_view()(request, 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_status_get(self):
        url = reverse('statuses:status_detail', kwargs={'pk':'1'})
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = StatusDetail.as_view()(request, 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
                 {
                    'name': u'inprogress', 'order_number': 1, 'url':  u'http://testserver/status/status/1/',
                    'project': u'http://testserver/projects/1/'
                 }
        )

    def test_status_delete_not_found(self):
        url = reverse('statuses:status_detail', kwargs={'pk':'6'})
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.delete(url)

        force_authenticate(request, user=user)
        response = StatusDetail.as_view()(request, 6)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestStatusFilter(APITestCase):
    fixtures = ['data_with_gravatar.json']

    def test_status_filter(self):
        url = reverse('statuses:status') + '?project=1'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = StatusView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                        'name':u'inprogress', 'order_number': 1, 'url':  u'http://testserver/status/status/1/',
                        'project': u'http://testserver/projects/1/'
                    },
                    {
                        'name':u'done', 'order_number': 2, 'url':  u'http://testserver/status/status/2/',
                        'project': u'http://testserver/projects/1/'
                    }
            ]
        )

    def test_status_filter_search(self):
        url = reverse('statuses:status') + '?search=inprogress'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = StatusView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    'name':u'inprogress', 'order_number': 1, 'url':  u'http://testserver/status/status/1/',
                    'project': u'http://testserver/projects/1/'
                },
                {
                    'name':u'inprogress1', 'order_number': 1, 'url':  u'http://testserver/status/status/3/',
                    'project': u'http://testserver/projects/2/'
                }
            ]
        )

    def test_status_filter_ordering(self):
        url = reverse('statuses:status') + '?ordering=project'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = StatusView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                {
                    'name':u'done', 'order_number': 2, 'url':  u'http://testserver/status/status/2/',
                    'project': u'http://testserver/projects/1/'
                },
                {
                    'name':u'inprogress', 'order_number': 1, 'url':  u'http://testserver/status/status/1/',
                    'project': u'http://testserver/projects/1/'
                },
                {
                    'name': u'done', 'order_number': 2, 'url': u'http://testserver/status/status/4/',
                    'project': u'http://testserver/projects/2/'
                },
                {
                    'name':u'inprogress1', 'order_number': 1, 'url':  u'http://testserver/status/status/3/',
                    'project': u'http://testserver/projects/2/'
                },
            ]
        )

    def test_status_filter_search_ordering(self):
        url = reverse('statuses:status') + '?search=done&ordering=-project'
        user = get_user_model().objects.get(username='yura')

        factory = APIRequestFactory()
        request = factory.get(url)

        force_authenticate(request, user=user)
        response = StatusView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            [
                 {
                    'name': u'done', 'order_number': 2, 'url': u'http://testserver/status/status/4/',
                    'project': u'http://testserver/projects/2/'
                },
                {
                    'name':u'done', 'order_number': 2, 'url':  u'http://testserver/status/status/2/',
                    'project': u'http://testserver/projects/1/'
                },
            ]
        )

