from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from rest_framework import generics, permissions
from .models import Book, User, Note
from .serializers import BookSerializer, UserSerializer, NoteSerializer
from .permissions import IsOwnerOrReadOnly



class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.requests.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NoteList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class=NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.requests.user)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format),
        'notes': reverse('notes-list', request=request, format=format),
    })