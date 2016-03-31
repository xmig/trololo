from django.conf.urls import url
from activity import views


urlpatterns = [
    # <type>
    # a - all activity
    # p - project activity only
    # t - task activity only
    url('^(?P<show_type>[apt])/$', views.Activities.as_view(), name='activities'),
    url('^(?P<id>\d+)/$', views.SingleActivity.as_view(), name='single_activity')
]