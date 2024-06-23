# Generated by Django 5.0.6 on 2024-06-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название фотографии')),
                ('low_descrtiption', models.TextField(max_length=200, verbose_name='Кратко описание фотографии')),
                ('full_description', models.TextField(max_length=1000, verbose_name='Полное описание фотографии')),
                ('image', models.ImageField(upload_to='static/mainapp/image/', verbose_name='Фотография')),
            ],
        ),
    ]
