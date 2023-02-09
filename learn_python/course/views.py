import django.shortcuts


def overview(request):
    template_name = 'course/overview.html'
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
    )
