from django.contrib import admin
from .models import Book, User, Note
# Register your models here.

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Note)