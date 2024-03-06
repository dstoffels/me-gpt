from .models import Chat, Message
from rest_framework import serializers
from users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    index = serializers.IntegerField(required=False)

    class Meta:
        model = Message
        fields = "id", "role", "content", "index"


class ChatSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = "id", "user_id", "title", "messages"

    def get_messages(self, chat: Chat):
        messages = chat.messages.all().order_by("index")
        return MessageSerializer(messages, many=True).data
