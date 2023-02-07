import django.contrib.admin
import django.urls


urlpatterns = [
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('', django.urls.include('main.urls')),
]
