from django.conf.urls import url
from views import load_balancer
from django.conf.urls import url, include
from rest_framework import routers
from views import ClusterInfoViewSet
from views import cluster_info_page, cluster_info_add #, cluster_info_edit
from webtools import health_check



router = routers.DefaultRouter()
router.register(r'cluster_info', ClusterInfoViewSet)


urlpatterns = [
    url(r'^load_balancer/$', load_balancer, name='load_balanser'),
    url(r'^cluster_info/api/', include(router.urls)),

    url(r'^cluster_info/$', cluster_info_page),
    url(r'^cluster_info_add/$', cluster_info_add),
    url(r'^health_check/$', health_check, name='health_check'),

]