from django.conf.urls import url
from projects import views



urlpatterns = [
    url(r'^tasks/$', views.TaskData.as_view(), name='tasks'),
    url(r'^projects/$', views.ProjectList.as_view(), name='projects'),
    url(r'^projects/(?P<pk>.+)/$', views.ProjectDetail.as_view(), name='projects_detail'),


    # url(r'^$', views.project_list, name='projects'),
    # url(r'^create/$', projects.views.project_create, name='project_create'),
    # url(r'^(?P<project_id>[0-9]+)/$', projects.views.project_edit, name='project_edit'),
    # url(r'^(?P<project_id>[0-9]+)/details$', projects.views.project_details, name='project_details'),
    # url(r'^(?P<project_id>[0-9]+)/delete$', projects.views.project_delete, name='project_delete')


]
