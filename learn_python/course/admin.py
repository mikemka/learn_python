from django.contrib import admin
from course.models import Example, Task, Lesson, Course, Tag


admin.AdminSite.site_header = 'Cервисы администрирования'
admin.AdminSite.site_title = 'Cервисы администрирования'
admin.AdminSite.index_title = 'Python-хендбук'


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
    list_display = ('title', 'is_published')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'render_tag', 'render_tag_outline')
    list_display_links = ('name', 'render_tag', 'render_tag_outline')
    fields = ('name', 'background_color', 'render_tag', 'render_tag_outline')
    readonly_fields = ('render_tag', 'render_tag_outline')
