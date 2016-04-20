from django.conf.urls import url
from projects.views import TaskCommentDetail, TaskCommentList


urlpatterns = [ url(r'^$', TaskCommentList.as_view(), name='comments'),
                url(r'^(?P<pk>[0-9]+)/$', TaskCommentDetail.as_view(), name='comments_detail')
]
