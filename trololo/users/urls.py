from django.conf.urls import url
from users import views


urlpatterns = [
    url(r'^$', views.UserListView.as_view(), name='user_list'),
    url(r'^profile/$', views.UserProfile.as_view(), name='user_profile'),


    # url(r'^(?P<pk>[0-9]+)/$', views.SingleUser.as_view(), name='users_list'),
    # url(r'^users_list/$', views.UsersList.as_view(), name='users_list'),
    url('^(?P<id>\d+)/$', views.SingleUser.as_view(), name='single_user')
]