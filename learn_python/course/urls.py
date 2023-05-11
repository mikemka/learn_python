import course.views
import django.urls


urlpatterns = [
    django.urls.path('', course.views.overview, name='course_overview'),
    django.urls.path('<int:pk>/', course.views.introduction, name='course_introduction'),
    django.urls.path('lesson/<int:pk>/', course.views.lesson, name='course_lesson'),
    django.urls.path('task/<int:pk>/', course.views.task, name='course_task'),
]
