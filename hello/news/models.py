from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Data')

    def __str__(self):
        return f'News {self.title}' #для красоты

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
