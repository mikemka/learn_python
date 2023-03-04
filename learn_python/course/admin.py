from django.contrib import admin
from course.models import Example, Task, Lesson, Course


admin.AdminSite.site_header = 'Cервисы администрирования'
admin.AdminSite.site_title = 'Cервисы администрирования'
admin.AdminSite.index_title = 'Cервисы администрирования'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'get_time_limit', 'get_memory_limit', 'difficulty')
    list_display_links = ('title',)


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'task')
    list_display_links = ('id', 'task')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)
