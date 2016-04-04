from django.conf.urls import url
from projects import views


urlpatterns = [
    url(r'^$', views.TaskList.as_view(), name='tasks'),
    url(r'^(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='tasks_detail'),

]
