import course.views
import django.urls


urlpatterns = [
    django.urls.path('', course.views.overview, name='course_overview'),
    django.urls.path('<int:pk>/', course.views.introduction, name='course_introduction'),
]
