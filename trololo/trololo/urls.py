from django.conf.urls import include, url
from django.contrib import admin
from users import urls as users_urls
from users.views import AccountConfirmEmailView, MainView
from django.conf import settings

from rest_framework import routers
from projects import views_api
# from users import views


router = routers.DefaultRouter()
router.register(r'projects', views_api.ProjectViewSet)
router.register(r'tasks', views_api.TaskViewSet)
router.register(r'projectscomments', views_api.ProjectCommentViewSet)
router.register(r'taskscomments', views_api.TaskCommentViewSet)
# router.register(r'users', views.UserProfile)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^users/', include(users.urls)),
    url(r'^users/', include(users_urls, namespace="users")),
    url(r'^api/', include(router.urls)),
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
