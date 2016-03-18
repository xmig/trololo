from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
import requests
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth import get_user_model


# class CsrfExemptSessionAuthentication(SessionAuthentication):
#     """Helper Class to ignore Csrf Token verification"""
#     def enforce_csrf(self, request):
#         return  # To not perform the csrf check previously happening


class SingleUser(GenericAPIView):
    """
        Get user's data by it's id
    """
    queryset = get_user_model().objects.all()

    def get(self, request, id):
        try:
            user = self.get_queryset().get(pk=int(id))
        except get_user_model().DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        user_data = UserSerializer(user).data

        # TODO: hide some data for not current user
        # if user_data['id'] != request.user.id:
        #     pass
        return Response(user_data)


from users.models import TrololoUser
from django.http import Http404


class UsersList(GenericAPIView):
    """
    Get List of Users.
    """
    serializer_class = UserSerializer
    queryset = TrololoUser.objects.all()

    def get(self, request):

        return Response(
            UserSerializer(self.get_queryset(), many=True).data
        )


class SingleUser(GenericAPIView):
    """
    Retrieve, update or delete User instance.
    """
    serializer_class = UserSerializer


    def get_object(self, pk):
        try:
            return TrololoUser.objects.get(pk=pk)
        except TrololoUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        single_user = self.get_object(pk)
        serializer = UserSerializer(single_user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        single_user = self.get_object(pk)
        serializer = UserSerializer(single_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        single_user = self.get_object(pk)
        single_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class UserProfile(GenericAPIView):
    """
        Get/Update current logged in user profile data.
    """
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get(self, request):
        u = self.get_serializer_class()(request.user)

        return Response(u.data)

    def put(self,request):
        s = self.get_serializer_class()(request.user, data=request.data)

        if s.is_valid():
            s.save()

            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response({"errors": s.errors}, status=status.HTTP_400_BAD_REQUEST)


class AccountConfirmEmailView(APIView):
    authentication_classes = ()
    permission_classes = ()
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, key, format=None):
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