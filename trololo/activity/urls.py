from django.conf.urls import url
from activity import views


urlpatterns = [
    url(r'^project/(?P<id>\d+)/$', views.ProjectActivity.as_view(), name='project_activity'),
    url('^(?P<id>\d+)/$', views.SingleActivity.as_view(), name='single_activity')
]