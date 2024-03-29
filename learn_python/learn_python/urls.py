import django.conf
import django.urls


urlpatterns = [
    django.urls.path('course/', django.urls.include('course.urls')),
    django.urls.path('users/', django.urls.include('users.urls')),
    django.urls.path('', django.urls.include('main.urls')),
]

if django.conf.settings.DEBUG:
    urlpatterns += [
        django.urls.path('__debug__/', django.urls.include('debug_toolbar.urls')),
    ]
