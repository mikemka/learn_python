import django.shortcuts
import course.models
import django.db.models


def overview(request):
    template_name = 'course/overview.html'
    context = {
        'courses': course.models.Course.objects.filter(is_published=True).prefetch_related('tags'),
    }
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
        context=context
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
    context['lessons'] = course.models.Lesson.objects.filter(course=context['course'])
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
        context=context
    )
