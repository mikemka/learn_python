import django.shortcuts
import course.models
import django.db.models
from django.http import HttpResponseNotFound


def overview(request):
    template_name = 'course/overview.html'
    
    courses_private = course.models.Course.objects.filter(is_published=True, private=True).prefetch_related('tags', 'access')
    materials = course.models.PrivateMaterial.objects.filter(is_published=True).prefetch_related('access')
    
    context = {
        'courses': course.models.Course.objects.filter(is_published=True, private=False).prefetch_related('tags'),
        'courses_private': [i for i in courses_private if request.user in i.access.all()],
        'materials': [i for i in materials if request.user in i.access.all()],
    }
    
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
        context=context,
    )


def introduction(request, pk: int):
    template_name = 'course/introduction.html'
    
    context = {
        'course': django.shortcuts.get_object_or_404(
            course.models.Course.objects,
            id=pk,
            is_published=True,
        ),
    }
    context['lessons'] = course.models.Lesson.objects.filter(
        course=context['course'],
        is_published=True,
    )
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
        context=context,
    )


def lesson(request, pk: int):
    template_name = 'course/lesson.html'
    
    context = {
        'lesson': django.shortcuts.get_object_or_404(
            course.models.Lesson.objects,
            id=pk,
            is_published=True,
        ),
    }
    context['tasks'] = course.models.Task.objects.filter(
        lesson=context['lesson'],
        is_published=True,
    ).order_by('difficulty')
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
        context=context,
    )


def task(request, pk: int):
    template_name = 'course/task.html'
    
    context = {
        'task': django.shortcuts.get_object_or_404(
            course.models.Task.objects,
            id=pk,
            is_published=True,
        ),
    }
    context['examples'] = course.models.Example.objects.filter(
        task=context['task'],
        is_published=True,
    )
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
        context=context,
    )


def material(request, pk: int):
    template_name = 'course/material.html'
    
    material = django.shortcuts.get_object_or_404(
        course.models.PrivateMaterial,
        id=pk,
        is_published=True,
    )

    context = {
        'material': material,
    }
    
    if request.user not in material.access.all():
        return HttpResponseNotFound()
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
        context=context,
    )
