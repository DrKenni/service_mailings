# Generated by Django 4.2.5 on 2023-09-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_initial'),
        ('mailing', '0004_alter_log_mailing'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='client',
            field=models.ManyToManyField(to='client.client', verbose_name='клиент'),
        ),
    ]