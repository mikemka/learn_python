import django.contrib.admin
import django.urls


urlpatterns = [
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('course/', django.urls.include('course.urls')),
    django.urls.path('tinymce/', django.urls.include('tinymce.urls')),
    django.urls.path('', django.urls.include('main.urls')),
]
