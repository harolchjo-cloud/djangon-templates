from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_ui, name='chat_ui'),
    path('api/message/', views.message_api, name='chat_message_api'),
]
