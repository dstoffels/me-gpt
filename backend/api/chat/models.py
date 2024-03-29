from django.db import models


class Chat(models.Model):
    pass


class Message(models.Model):
    ROLES = ["system", "user", "assistant"]
    chat = models.ForeignKey(Chat, related_field="messages")
    role = models.CharField(max_length=10, choices=[(role, role) for role in ROLES])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
