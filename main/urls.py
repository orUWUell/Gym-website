
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main_view, name='homepage'),
    path('search/', views.SearchView.as_view(), name='search'),


]
