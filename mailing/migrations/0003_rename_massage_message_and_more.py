# Generated by Django 4.2.5 on 2023-09-12 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Massage',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='mailing',
            old_name='massage',
            new_name='message',
        ),
    ]