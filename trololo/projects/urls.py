from django.conf.urls import url
from projects import views


urlpatterns = [

    url(r'^projects/$', views.ProjectsList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)$', views.ProjectDetail.as_view()),

    url(r'^tasks/$', views.TaskList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)$', views.TaskDetail.as_view()),

]