from typing import Iterable
from django.db import models


class Chat(models.Model):
    user = models.ForeignKey(
        "users.User", related_name="chats", on_delete=models.CASCADE
    )
    title = models.TextField()

    messages: models.QuerySet = None


class Message(models.Model):
    ROLES = ["user", "assistant"]
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    index = models.PositiveIntegerField()
    role = models.CharField(max_length=10, choices=[(role, role) for role in ROLES])
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["index"]

    def save(self, *args, **kwargs) -> None:
        """The message model automates indexing on save to ensure proper ordering within its chat"""
        messages = Message.objects.filter(chat=self.chat)
        count = messages.count()
        if self.pk is None:
            self.index = count
        else:
            original_index = messages.get(pk=self.pk).index
            if self.index >= count:
                self.index = count - 1
            if self.index != original_index:
                if original_index > self.index:
                    messages.filter(
                        index__lt=original_index, index__gte=self.index
                    ).update(index=models.F("index") + 1)
                else:
                    messages.filter(
                        index__gt=original_index, index__lte=self.index
                    ).update(index=models.F("index") - 1)
        super().save(*args, **kwargs)
