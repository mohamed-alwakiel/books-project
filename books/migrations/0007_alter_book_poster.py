# Generated by Django 4.0.4 on 2022-04-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='poster',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
