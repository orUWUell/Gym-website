from django.urls import path 
from . import views 

urlpatterns = [
    path('<int:pk>', views.chat_view, name='chat'),
    path('create/', views.create_room, name='create'),
    path('delete/<int:pk>/<int:user_id>', views.delete_message, name='delete'),
]