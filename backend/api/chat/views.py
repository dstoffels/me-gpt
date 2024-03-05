from rest_framework import generics
from .serializers import ChatSerializer, MessageSerializer

class ChatsView(generics.ListCreateAPIView):
    serializer_class = ChatSerializer

class MessagesView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer