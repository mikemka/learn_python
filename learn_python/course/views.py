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
