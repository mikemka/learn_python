from django.shortcuts import render


def homepage(request):
    template_name = 'main/homepage.html'
    
    return render(
        request=request,
        template_name=template_name,
    )
