# Generated by Django 4.1.3 on 2022-11-10 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_rename_desire_status_status_status_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='my_owner',
            new_name='user',
        ),
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Mystery', 'Mystery'), ('Sci-Fi', 'Sci-Fi'), ('Fantasy', 'Fantasy'), ('Action-and-Adventure', 'Action-and-Adventure'), ('Nonfiction', 'Nonfiction'), ('Thriller', 'Thriller'), ('Horror', 'Horror'), ('Historical-Fiction', 'Historical-Fiction')], default='Mystery', max_length=50),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('Reading', 'Reading'), ('Intersted', 'Intersted'), ('want-to-read', 'want-to-read')], default='Intersted', max_length=50),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, max_length=10000, null=True)),
                ('private', models.BooleanField(default=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
