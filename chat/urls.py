from django.urls import path 
from . import views 

urlpatterns = [
    path('<int:pk>', views.chat_view, name='create'),
]