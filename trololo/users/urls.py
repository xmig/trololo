from django.conf.urls import url
from users import views


urlpatterns = [
    url(r'^$', views.UserListView.as_view(), name='user_list'),
    url(r'^profile/$', views.UserProfile.as_view(), name='user_profile'),
    url('^(?P<id>\d+)/$', views.SingleUser.as_view(), name='single_user'),
    url(r'^social_links/$', views.SocialLinksAddUser.as_view(), name='social_links'),
]