from typing import Iterable
from django.db import models


class Chat(models.Model):
    user = models.ForeignKey(
        "users.User", related_name="chats", on_delete=models.CASCADE
    )


class Message(models.Model):
    ROLES = ["system", "user", "assistant"]
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    role = models.CharField(max_length=10, choices=[(role, role) for role in ROLES])
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        return super().save(force_insert, force_update, using, update_fields)
