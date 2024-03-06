from rest_framework import generics, permissions
from .serializers import ChatSerializer, MessageSerializer, Message, Chat

class ChatsView(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = permissions.IsAuthenticated,
    
    def get_queryset(self):
        return Chat.objects.filter(user_id=self.request.user.id)
    
    def perform_create(self, serializer: ChatSerializer):
        serializer.validated_data['user_id'] = self.request.user.id
        return super().perform_create(serializer)

class ChatView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChatSerializer
    lookup_url_kwarg = 'chat_id'
    permission_classes = permissions.IsAuthenticated,
    queryset = Chat.objects.all()
    

class MessagesView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer: MessageSerializer):
        chat_id = self.kwargs.get('chat_id')
        serializer.validated_data['chat_id'] = chat_id
        serializer.save()

class MessageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    lookup_url_kwarg = 'message_id'
    
    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat_id=chat_id)