# Generated by Django 4.0.4 on 2022-04-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='appropriate',
            field=models.CharField(choices=[('un', 'Under 8'), ('bt', 'Between 8-15'), ('ad', 'Adults')], default='bt', max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='poster',
            field=models.ImageField(upload_to='books/static/books'),
        ),
    ]