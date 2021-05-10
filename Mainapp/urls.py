
from django.contrib import admin
from django.urls import path,include
from Mainapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home , name='home'),
    path('login/',views.login , name='Login'),
    path('login/login_tenant',views.login_tenant , name='Login'),
    path('login/register_tenant',views.register_tenant),
    path('login/register_owner',views.register_owner),
    path('profile_tenant/',views.tenant_profile ,name='Profile'),
    path('profile_owner/',views.owner_profile , name='profile'),
    path('aboutus/',views.aboutus , name='AboutUs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
