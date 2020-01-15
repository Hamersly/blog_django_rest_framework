from django.shortcuts import render

from rest_framework import viewsets #Возможно сделать и таким образом
from django.contrib.auth import get_user_model
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from .serializers import PostSerializer, UserSerializer


# class PostViewSet(viewsets.ModelViewSet): #Возможно сделать и таким образом
# 	permission_classes = (IsAuthorOrReadOnly,)
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer


# class UserViewSet(viewsets.ModelViewSet): #Возможно сделать и таким образом
# 	queryset = get_user_model().objects.all()
# 	serializer_class = UserSerializer


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer