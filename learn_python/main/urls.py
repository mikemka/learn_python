import django.urls
import main.views


urlpatterns = [
    django.urls.path('', main.views.homepage, name='homepage'),
]
