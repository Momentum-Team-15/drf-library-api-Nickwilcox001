# Generated by Django 4.1.3 on 2022-11-14 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_book_genre_alter_status_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tracked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Mystery', 'Mystery'), ('Action-and-Adventure', 'Action-and-Adventure'), ('Horror', 'Horror'), ('Thriller', 'Thriller'), ('Fantasy', 'Fantasy'), ('Sci-Fi', 'Sci-Fi'), ('Historical-Fiction', 'Historical-Fiction'), ('Nonfiction', 'Nonfiction')], default='Mystery', max_length=50),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('Reading', 'Reading'), ('want-to-read', 'want-to-read'), ('Intersted', 'Intersted')], default='Intersted', max_length=50),
        ),
    ]
