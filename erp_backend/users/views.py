# users/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from .permissions import IsAdmin, IsManager

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.user.role == 'ADMIN':
            return [permissions.IsAuthenticated()]
        elif self.request.user.role == 'MANAGER':
            return [permissions.IsAuthenticated()]
        return []

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
