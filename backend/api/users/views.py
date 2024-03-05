from rest_framework import generics
from .serializers import RegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime
from .models import User
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        # login user
        user: User = authenticate(request, email=request.data.get('email'), password=request.data.get('password'))

        if user:
            user.last_login = datetime.now()
            user.save()

        # # Generate JWT
        refresh: RefreshToken = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)}, status=201)
        

