from django.db import models


class Bulletin(models.Model):
    title = models.CharField('заголовок', max_length=255)
    description = models.TextField('описание')
    pub_date = models.DateTimeField('опубликовано', auto_now_add=True, null=True)
    upd_date = models.DateTimeField('обновлено', auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)
