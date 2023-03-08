import django.shortcuts
import course.views


def homepage(request):
    if request.user.is_authenticated:
        return course.views.overview(request=request)
    
    template_name = 'main/homepage.html'
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
    )
