from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
# from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from rest_framework.authentication import SessionAuthentication
# from rest_framework import permissions
# from django.contrib.auth import get_user_model


# class UserList(APIView):
#     # authentication_classes = (SessionAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request):
#         User = get_user_model()
#
#         return Response(
#             UserSerializer(User.objects.all(), many=True).data
#         )
#
#     def post(self, request):
#         s = UserSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#
#             return Response(s.data, status=status.HTTP_201_CREATED)
#
#         return Response({"errors": s.errors}, status=status.HTTP_400_BAD_REQUEST)


# class CsrfExemptSessionAuthentication(SessionAuthentication):
#
#     def enforce_csrf(self, request):
#         return  # To not perform the csrf check previously happening


# class SingleUser(APIView):
#     # authentication_classes = (SessionAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request, id):
#         try:
#             user = get_user_model().objects.get(pk=id)
#         except get_user_model().DoesNotExist:
#             return Response({}, status=status.HTTP_404_NOT_FOUND)
#
#         return Response(UserSerializer(user).data)
#
#     def put(self, request, id):
#         s = UserSerializer(data=request.data, photo=request.data['file'])
#         if s.is_valid():
#             s.save()
#
#             return Response(s.data, status=status.HTTP_200_OK)
#
#         return Response({"errors": s.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(APIView):
    # parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request):
        u = UserSerializer(request.user)

        return Response(u.data)

    def put(self,request):
        s = UserSerializer(request.user, data=request.data)

        if s.is_valid():
            s.save()

            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response({"errors": s.errors}, status=status.HTTP_400_BAD_REQUEST)


class AccountConfirmEmailView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, key):
        r = requests.post(
            request.build_absolute_uri(reverse('registration:rest_verify_email')),
            # 'http://localhost:{}/rest-auth/registration/verify-email/'.format(settings.SERVER_PORT),
            json={"key": key}
        )

        if r.status_code == 200:
            return Response({"STATUS": "REGISTRATION COMPLETED"}, status=status.HTTP_200_OK)
        else:
            return Response({"STATUS": r.raw}, status=r.status_code)


class MainView(TemplateView):
    template_name = 'templates/index.html'