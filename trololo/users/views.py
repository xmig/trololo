from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
import requests
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth import get_user_model
from rest_framework import filters
from django_filters import FilterSet, NumberFilter, IsoDateTimeFilter


# class CsrfExemptSessionAuthentication(SessionAuthentication):
#     """Helper Class to ignore Csrf Token verification"""
#     def enforce_csrf(self, request):
#         return  # To not perform the csrf check previously happening


class SingleUser(GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get(self, request, id):
        """
        Get user's data by it's id
        """
        try:
            user = self.get_queryset().get(pk=int(id))
        except get_user_model().DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        user_data = self.get_serializer_class()(user, context={'request': request}).data

        # TODO: hide some data for not current user
        # if user_data['id'] != request.user.id:
        #     pass
        return Response(user_data)


class UserProfile(GenericAPIView):
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request):
        """
        Get current user profile info
        """
        u = self.get_serializer_class()(request.user, context={'request': request})

        return Response(u.data)

    def put(self,request):
        """
            Update current user profile info
        """
        s = self.get_serializer_class()(request.user, data=request.data, context={'request': request}, partial=True)

        if s.is_valid():
            s.save()

            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response({"detail": s.errors}, status=status.HTTP_400_BAD_REQUEST)


class UsersFilter(FilterSet):
    project = NumberFilter(name='projects_added__pk')
    task = NumberFilter(name='tasks_added__pk')
    logged_min = IsoDateTimeFilter(name='last_login', lookup_type='gte')
    logged_max = IsoDateTimeFilter(name='last_login', lookup_type='lte')

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name',
            'department', 'specialization',
            'detailed_info', 'email',
            'logged_max', 'logged_min', 'project', 'task'
        )


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.prefetch_related("projects_added", "tasks_added").all()
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UsersFilter
    ordering_fields = (
        'username', 'first_name', 'last_name', 'department', 'specialization', 'detailed_info', 'email', 'id'
    )
    search_fields = ('username', 'first_name', 'last_name', 'department', 'specialization', 'detailed_info', 'email')


class AccountConfirmEmailView(APIView):
    authentication_classes = ()
    permission_classes = ()
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, key, format=None):
        """
        Send confirmation request for given key and renders email confirmation status page.

            * key: verification key

            return: rendered HTML template 'account_confirm.html'
        """
        r = requests.post(
            request.build_absolute_uri(reverse('registration:rest_verify_email')),
            # 'http://localhost:{}/rest-auth/registration/verify-email/'.format(settings.SERVER_PORT),
            json={"key": key}
        )

        status = 'REGISTRATION COMPLETED' if r.status_code == 200 else r.raw

        return Response(
            {"status": status}, template_name='account_confirm.html', status=r.status_code
        )


class MainView(TemplateView):
    template_name = 'index.html'


class EmailVerificationSentView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        return Response("Verification email has been sent.")