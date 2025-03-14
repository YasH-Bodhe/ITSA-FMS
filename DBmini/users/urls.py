from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'), # the name given to the urls is used inide the html like {% urls 'index' %}
    path('register/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'), # for user login
    path('adminlogin/', views.adminlogin_view, name='admin_login'), # for admin login
    path('home/',views.home, name='home'),
    path('event/<int:event_id>/register/', views.register_event, name='register_event'),
    path('registrations/<int:event_id>/', views.event_registrations, name='event_registrations'),
    # path('registration/success/', views.registration_success, name='registration_success'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('home/profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('manage-registrations/', views.manage_registrations, name='manage_registrations'),
    path('delete-registration/<int:registration_id>/', views.delete_registration, name='delete_registration'),
]

if settings.DEBUG:  # Ensure this only runs in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)