from django.db import models

from users.models import User, NULLABLE


class Message(models.Model):
    title = models.CharField(max_length=300, verbose_name='заголовок')
    body = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'cообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    TIME_FREQUENCY_CHOICES = [
        (1, 'Раз в день'),
        (2, 'Раз в неделю'),
        (3, 'Раз в месяц'),
    ]

    STATUS_MAILING_CHOICES = [
        (1, 'Создана'),
        (2, 'Запущена'),
        (3, 'Завершена'),
    ]

    mailing_time = models.DateTimeField(auto_now_add=True, verbose_name='время рассылки')
    frequency = models.PositiveSmallIntegerField(choices=TIME_FREQUENCY_CHOICES, default=1,
                                                 verbose_name='переодичность рассылки')
    status = models.PositiveSmallIntegerField(choices=STATUS_MAILING_CHOICES, default=1,
                                              verbose_name='статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='cообщение', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Log(models.Model):
    server_response = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)
    date_attempts = models.DateTimeField(auto_now_add=True, verbose_name='дата попытки')
    status = models.CharField(max_length=100, verbose_name='статус попытки')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылки',  **NULLABLE)

    def __str__(self):
        return f"{self.date_attempts}: {self.status}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
