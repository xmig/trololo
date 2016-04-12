from django.conf.urls import url
from projects.views import ProjectCommentDetail, ProjectCommentList


urlpatterns = [
    url(r'^$', ProjectCommentList.as_view(), name='comments'),
    url(r'^(?P<pk>[0-9]+)/$', ProjectCommentDetail.as_view(), name='comments_detail')
]

