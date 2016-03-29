from django.conf.urls import url
from projects import views


urlpatterns = [

    url(r'^projects/$', views.ProjectsList.as_view(), name='projects'),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='projects_detail'),
    url(r'^tasks/$', views.TaskList.as_view(), name='tasks'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='tasks_detail'),

    # <type>
    # a - all activity
    # p - project activity only
    # t - task activity only
    url(r'^projects/(?P<id>\d+)/(?P<show_type>[apt])/activity$', views.ProjectActivity.as_view(), name='project_activity'),
]
