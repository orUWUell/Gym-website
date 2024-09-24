from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('', include("django.contrib.auth.urls"), name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/<int:pk>', views.update_profile, name='edit_profile'),
]