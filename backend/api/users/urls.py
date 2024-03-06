from django.urls import path
from .views import RegisterView, LoginView, UserView

urlpatterns = [
    path("", UserView.as_view()),
    path("/register", RegisterView.as_view()),
    path("/login", LoginView.as_view()),
]
