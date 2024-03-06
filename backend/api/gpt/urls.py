from django.urls import path
from .views import GPTPromptView, GPTFineTuneView

urlpatterns = [
    path("", GPTPromptView.as_view()),
    path("/finetune", GPTFineTuneView.as_view()),
]
