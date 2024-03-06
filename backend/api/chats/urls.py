from django.urls import path
from .views import ChatsView, ChatView, MessagesView, MessageView, RolesView

urlpatterns = [
    path("", ChatsView.as_view()),
    path("/roles", RolesView.as_view()),
    path("/<int:chat_id>", ChatView.as_view()),
    path("/<int:chat_id>/messages", MessagesView.as_view()),
    path("/<int:chat_id>/messages/<int:message_id>", MessageView.as_view()),
]
