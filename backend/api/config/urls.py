from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user", include("users.urls")),
    path("chats", include("chats.urls")),
    path("gpt", include("gpt.urls")),
]
