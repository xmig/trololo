from django.conf.urls import url
from users import views


urlpatterns = [
    url('^login/$', views.app_login),
    url('^user/$', views.user_list),
    url('^users/$', views.UserList.as_view()),
    url('^(?P<id>\d+)/$', views.SingleUser.as_view())
]