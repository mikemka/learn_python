import django.urls
import users.views


urlpatterns = [
    django.urls.path('', users.views.login),
    django.urls.path('login/', users.views.login, name='login'),
]
