from django.urls import path
from .views import ChatsView, MessagesView

urlpatterns = [
    path('', ChatsView.as_view()),
    path('messages', MessagesView.as_view()),
]