from django.db import models

from users.models import User, NULLABLE


class Client(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    surname = models.CharField(max_length=150, verbose_name='отчество', **NULLABLE)
    comment = models.CharField(max_length=400, verbose_name='комментарий')
    contact_email = models.EmailField(verbose_name='контактная почта')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='активация',**NULLABLE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
