from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Album(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание', null=True, blank=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор',
                               related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата-время создания")
    isPrivate = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}.{self.title}'

    class Meta:
        db_table = 'Albums'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'



