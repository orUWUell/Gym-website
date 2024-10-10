from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('', include("django.contrib.auth.urls"), name='login'),
    path('profile/<int:pk>', views.profile_view, name='profile'),
    path('edit_profile/<int:pk>', views.EditProfileView.as_view(), name='edit_profile'),
]