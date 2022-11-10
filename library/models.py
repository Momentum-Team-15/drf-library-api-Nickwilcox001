from django.db import models
from django.contrib.auth.models import AbstractUser
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class User(AbstractUser):
    pass

GENRES={
    ('Fantasy', 'Fantasy'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Action-and-Adventure', 'Action-and-Adventure'),
    ('Mystery', 'Mystery'),
    ('Horror', 'Horror'),
    ('Thriller', 'Thriller'),
    ('Historical-Fiction', 'Historical-Fiction'),
    ('Nonfiction', 'Nonfiction'),
}

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publish_date = models.DateField()
    genre = models.CharField(max_length=50, default='Mystery', choices = GENRES)
    featured = models.BooleanField(default=False)

STATUS_CHOICES = {
    ('Reading', 'Reading'),
    ('want-to-read','want-to-read'),
    ('Intersted', 'Intersted'),
}


class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=50, default='Intersted', choices=STATUS_CHOICES)

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length =10000, blank=True, null=True)
    private = models.BooleanField(default=True)