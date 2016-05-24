from django.conf.urls import url
from projects.views import TaskFileList, TaskFileDetail

urlpatterns = [
    url(r'^$', TaskFileList.as_view(), name='task_file'),
    url(r'^(?P<pk>[0-9]+)/$', TaskFileDetail.as_view(), name='task_file_detail')
]

