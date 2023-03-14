import django.contrib.admin
import django.urls
import users.views


urlpatterns = [
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('logout/', users.views.logout_user, name='logout'),
    django.urls.path('profile/', users.views.profile, name='profile'),
    django.urls.path('login/', users.views.LoginUser.as_view(), name='login'),
    django.urls.path('registration/', users.views.RegisterUser.as_view(), name='registration'),
]
