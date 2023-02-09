import course.views
import django.urls


urlpatterns = [
    django.urls.path('', course.views.overview, name='course_overview'),
]
