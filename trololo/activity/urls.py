from django.conf.urls import url
from activity import views


urlpatterns = [
    url('^(?P<id>\d+)/$', views.SingleActivity.as_view(), name='single_activity')
]