# Generated by Django 4.2.5 on 2023-09-12 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='log',
            name='mailing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='рассылки'),
        ),
    ]
