from django.urls import path
from .views import ChatsView, ChatView, MessagesView

urlpatterns = [
    path('', ChatsView.as_view()),
    path('/<int:chat_id>', ChatView.as_view()),
    path('/messages', MessagesView.as_view()),
]