from django.conf.urls import url
from projects import views


urlpatterns = [

    url(r'^$', views.ProjectsList.as_view(), name='projects'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name='projects_detail'),


    # <type>
    # a - all activity
    # p - project activity only
    # t - task activity only
    url(r'^(?P<id>\d+)/(?P<show_type>[apt])/activity$', views.ProjectActivity.as_view(), name='project_activity'),
]
