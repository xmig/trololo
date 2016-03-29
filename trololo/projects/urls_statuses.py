from django.conf.urls import url
from projects import views
from projects.views_status import StatusDetail, StatusView


urlpatterns = [
    url(r'^status/$', StatusView.as_view(), name='status'),
    url(r'^status/(?P<pk>[0-9]+)/$', StatusDetail.as_view(), name='status_detail')
]
