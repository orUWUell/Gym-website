from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('', include("django.contrib.auth.urls"), name='login'),
    path('profile/<int:pk>', views.profile_view, name='profile'),
    path('logout_profile/', views.logout_view, name='logout_profile'),
    path('password/', views.CustomPasswordChangeView.as_view(template_name='registration/change_password.html'), name='change_password'),
    path('update_user/', views.update_user, name='update_user'),
]