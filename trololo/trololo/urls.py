from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from projects import views_api


router = routers.DefaultRouter()
router.register(r'projects', views_api.ProjectViewSet)
router.register(r'tasks', views_api.TaskViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'trololo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),

]
