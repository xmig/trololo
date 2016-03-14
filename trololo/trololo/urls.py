from django.conf.urls import include, url
from django.contrib import admin
from users import urls as users_urls
from users.views import AccountConfirmEmailView, MainView
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^users/', include(users.urls)),
    url(r'^users/', include(users_urls, namespace="users")),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>\w+)/$', AccountConfirmEmailView.as_view(),
        name='account_confirm_email'),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls', namespace='registration')),
    url(r'^$', MainView.as_view()),
]

# docs
if 'rest_framework_swagger' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^docs/', include('rest_framework_swagger.urls')),
    ]
