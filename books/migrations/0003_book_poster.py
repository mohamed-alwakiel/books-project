# Generated by Django 4.0.4 on 2022-04-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_isbn_book_description_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='poster',
            field=models.ImageField(default=16, upload_to='books'),
            preserve_default=False,
        ),
    ]