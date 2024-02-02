from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default=50)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title