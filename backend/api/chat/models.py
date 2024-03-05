from django.db import models


class Chat(models.Model):
    user = models.ForeignKey(
        "users.User", related_name="chats", on_delete=models.CASCADE
    )


class Message(models.Model):
    ROLES = ["system", "user", "assistant"]
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[(role, role) for role in ROLES])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
