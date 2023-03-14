import django.shortcuts


def login(request):
    template_name = 'users/login.html'
    
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
        # context=context
    )
