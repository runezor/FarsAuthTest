from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import UserSerializer

# View der viser alle users
class UserViewAll(generics.ListAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# View der bruges til at oprette users
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #Goor at vi ikke kan lave nye users medmindre vi er logget ind, obs: Alle users der er logget ind kan lave en ny user paa den her maade
    permission_classes = [permissions.IsAuthenticated]


# View der bruges til at vise/aendre en specifik user
class UserViewSpecific(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.all().order_by('-date_joined')
