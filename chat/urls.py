from django.urls import path 
from . import views 

urlpatterns = [
    path('<int:pk>', views.chat_view, name='chat'),
    path('create/', views.create_room, name='create'),
]