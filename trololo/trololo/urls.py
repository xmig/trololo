from django.conf.urls import include, url
from django.contrib import admin
from users import urls as users_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'trololo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^users/', include(users.urls)),
    url(r'^users/', include(users_urls, namespace="users")),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
