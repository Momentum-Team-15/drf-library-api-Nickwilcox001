from rest_framework import serializers
from .models import Book, Note
from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model

User = get_user_model()

class BookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'publish_date', 'user', 'tracked')

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'books')

class NoteSerializer(serializers.ModelSerializer):
    model = Note
    class Meta:
        fields =('user', 'book', 'created_at', 'updated_at', 'notes', 'private')