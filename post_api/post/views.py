from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics

# Create your views here.

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.order_by('-id')
    serializer_class = PostSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Post.objects.order_by('-id')
    
    def perform_update(self, serializer):
        serializer.save()