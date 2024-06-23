from django.db import models


class Photos(models.Model):
    title = models.CharField(verbose_name='Название фотографии', max_length=60)
    low_descrtiption = models.TextField(verbose_name='Кратко описание фотографии', max_length=200)
    full_description = models.TextField(verbose_name='Полное описание фотографии', max_length=1000)
    image = models.ImageField(verbose_name='Фотография', upload_to='static/mainapp/image/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
