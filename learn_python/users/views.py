import django.contrib.auth
import django.contrib.auth.views
import django.views.generic
import django.shortcuts
import django.urls
import users.forms


class RegisterUser(django.views.generic.CreateView):
    form_class = users.forms.RegisterUserForm
    template_name = 'users/registration.html'
    success_url = django.urls.reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs) | self.get_user_context(title="Регистрация")
    
    def get_user_context(self, **kwargs):
        return kwargs


class LoginUser(django.contrib.auth.views.LoginView):
    form_class = users.forms.LoginUserForm
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return django.urls.reverse_lazy('homepage')

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs) | self.get_user_context(title="Регистрация")
    
    def get_user_context(self, **kwargs):
        return kwargs


def logout_user(request):
    django.contrib.auth.logout(request)
    return django.shortcuts.redirect('login')


def profile(request):
    template_name = 'users/profile.html'
    
    if request.method == 'POST':
        form = users.forms.UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    form = users.forms.UpdateUserForm()

    return django.shortcuts.render(
        request=request,
        template_name=template_name,
        context={'form': form},
    )
