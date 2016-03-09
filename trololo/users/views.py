from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from users.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
import requests
from django.conf import settings

from django.core.urlresolvers import reverse


def app_login(request):
    if request.method == 'POST':
        user = request.POST['username']
        passwd = request.POST['password']

        user = authenticate(username=user, password=passwd)

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('/users/user/')

        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


@login_required
def user_list(request):
    return render(request, 'users.html', {'users_list': get_user_model().objects.all()})


class UserList(APIView):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

    # authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        User = get_user_model()
        print(User)

        return Response(
            UserSerializer(User.objects.all(), many=True).data
        )

    def post(self, request):
        s = UserSerializer(data=request.data)
        if s.is_valid():
            s.save()

            return Response(s.data, status=status.HTTP_201_CREATED)

        return Response({"errors": s.errors}, status=status.HTTP_400_BAD_REQUEST)


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class SingleUser(APIView):
    # authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        try:
            user = get_user_model().objects.get(pk=id)
        except get_user_model().DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        return Response(UserSerializer(user).data)

    def put(self, request, id):
        s = UserSerializer(data=request.data)
        if s.is_valid():
            s.save()

            return Response(s.data, status=status.HTTP_200_OK)

        return Response({"errors": s.errors}, status=status.HTTP_400_BAD_REQUEST)


class AccountConfirmEmailView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, key):
        r = requests.post(
            request.build_absolute_uri(reverse('account_confirm_email')),
            # 'http://localhost:{}/rest-auth/registration/verify-email/'.format(settings.SERVER_PORT),
            json={"key": key}
        )

        if r.status_code == 200:
            return Response({"STATUS": "REGISTRATION COMPLETED"}, status=status.HTTP_200_OK)
        else:
            return Response({"STATUS": r.raw}, status=r.status_code)
