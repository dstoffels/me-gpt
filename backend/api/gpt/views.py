import os
from django.conf import settings
from rest_framework import generics, response, request, permissions
from users.models import User
from openai import OpenAI
import json

openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def get_system_msg(user: User):
    return {
        "role": "system",
        "content": f"You are me. {user.info}. You will respond as me.",
    }


class GPTPromptView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: request.Request, *args, **kwargs):
        prompt = request.query_params.get("prompt")
        user = request.user
        return response.Response({"prompt": prompt, "user": user.id}, 200)


class GPTFineTuneView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request: request.Request, *args, **kwargs):
        user: User = request.user
        system_msg = get_system_msg(user)

        chats = user.chats.all().prefetch_related("messages")

        if len(chats) < 10:
            return response.Response(
                {
                    "message": "At least 10 chat examples are required to fine-tune your model."
                },
                400,
            )

        file_path = settings.BASE_DIR / "tmp/user_chats.jsonl"

        with open(file_path, "w") as file:
            for chat in chats:
                messages = [
                    {"role": message.role, "content": message.content}
                    for message in chat.messages.all()
                ]

                chat_data = {"messages": [system_msg, *messages]}
                file.write(json.dumps(chat_data) + "\n")

        try:
            file = openai.files.create(file=open(file_path, "rb"), purpose="fine-tune")

            job = openai.fine_tuning.jobs.create(
                training_file=file.id, model="gpt-3.5-turbo"
            )

            # cleanup
            openai.files.delete(file_id=file.id)

        except Exception as e:
            return response.Response(e.body, e.status_code)

        return response.Response(status=200)
