from django.conf.urls import include, url
from django.contrib import admin

from users import urls as users_urls
from projects import urls_projects as projects_urls
from projects import urls_tasks as tasks_urls
from projects import urls_statuses as statuses_urls
from projects import urls_comments_projects as comments_projects_urls
from projects import urls_comments_tasks as comments_tasks_urls
from projects import urls_task_files as task_files_urls
# from cluster import urls as cluster_urls

from projects.views import api_root, GlobalSearchView
from activity import urls as activity_urls

from users.views import (
    AccountConfirmEmailView, MainView, EmailVerificationSentView, SocialConnectionsView
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^api/$', api_root, name='api'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include(users_urls, namespace="users")),
    url(r'^status/', include(statuses_urls, namespace="statuses")),
    url(r'^projects/', include(projects_urls, namespace="projects")),
    url(r'^tasks/', include(tasks_urls, namespace="tasks")),
    url(r'^projects/comments/', include(comments_projects_urls, namespace="comments_projects")),
    url(r'^tasks/comments/', include(comments_tasks_urls, namespace="comments_tasks")),
    url(r'^tasks/files/', include(task_files_urls, namespace="tasks_files_detail")),
    url(r'^system/', include('cluster.urls', namespace="system")),

    url(r'^activities/', include(activity_urls, namespace="activity")),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>\w+)/$', AccountConfirmEmailView.as_view(),
        name='account_confirm_email'),
    url(r'^rest-auth/account-email-verification-sent/$',
        EmailVerificationSentView.as_view(), name='account_email_verification_sent'
    ),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls', namespace='registration')),
    url(r'^$', MainView.as_view()),

    url(r'^reset/done/', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'reset_done.html'}, name='password_reset_complete'
    ),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'password_reset_form.html', 'post_reset_redirect': '/'},
        name='password_reset_confirm'
    ),
    url(r'^accounts/social/connections/$',
        login_required(SocialConnectionsView.as_view()),
        name='socialaccount_connections'
    ),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^global_search/(?P<query_string>.*)/$', GlobalSearchView.as_view()),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url('^', include('django.contrib.auth.urls')),
]

# docs
if 'rest_framework_swagger' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^docs/', include('rest_framework_swagger.urls')),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)