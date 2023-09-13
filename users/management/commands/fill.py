from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from client.models import Client
from mailing.models import Message, Mailing


class Command(BaseCommand):
    def handle(self, *args, **options):

        Mailing.objects.all().delete()
        Message.objects.all().delete()
        Client.objects.all().delete()

        message_list = [
            {'id': 1, 'title': 'Welcome', 'body': 'Рад приветствовать, от всего сердца!'},
            {'id': 2, 'title': 'Распродажа одежды!', 'body': 'Скидки на все футболки 80%!'},
            {'id': 3, 'title': 'Праздничное настроение!', 'body': 'Приходите к нам и получите бурю эмоций!'}
        ]

        message_for_create = []

        for message in message_list:
            message_for_create.append(
                Message(**message)
            )

        Message.objects.bulk_create(message_for_create)

        client_list = [
            {'first_name': 'Andrew', 'last_name': 'Lavrov', 'surname': 'Romanovich', 'contact_email': 'test1@sky.pro'},
            {'first_name': 'Slava', 'last_name': 'Ushpil', 'surname': 'Andrevich', 'contact_email': 'test2@sky.pro'},
            {'first_name': 'Sergey', 'last_name': 'Savichev', 'surname': 'Ildarov', 'contact_email': 'test3@sky.pro'},
            {'first_name': 'Maria', 'last_name': 'Ruskih', 'surname': 'Petrovna', 'contact_email': 'test4@sky.pro'},
        ]
        client_for_create = []

        for client in client_list:
            client_for_create.append(
                Client(**client)
            )

        Client.objects.bulk_create(client_for_create)

        mailing_list = [
            {'frequency': 1, 'status': 1, 'message': Message.objects.get(pk=2)},
            {'frequency': 2, 'status': 3, 'message': Message.objects.get(pk=1)},
            {'frequency': 3, 'status': 2, 'message': Message.objects.get(pk=3)},
        ]
        mailing_for_create = []

        for mailing in mailing_list:
            mailing_for_create.append(
                Mailing(**mailing)
            )

        Mailing.objects.bulk_create(mailing_for_create)

        perm_group = Group.objects.create(name='manager')
        access_rights_manager = [
            'add_',
            'view_',
            'change_'
        ]
        parts = ['mailing', 'client']
        for part in parts:
            for right in access_rights_manager:
                perm = Permission.objects.get(content_type__app_label=part,
                                              content_type__model=part, codename=right+part)
                perm_group.permissions.add(perm)
