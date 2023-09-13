import smtplib
from datetime import datetime


from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from client.models import Client
from mailing.models import Mailing, Log


class Command(BaseCommand):
    def handle(self, *args, **options):
        mailing_list = Mailing.objects.filter(status=2)

        for mailing in mailing_list:
            client_list = [client.contact_email for client in Client.objects.filter(is_active=True)]
            if mailing.mailing_time == datetime.now():
                try:
                    send_mail(subject=mailing.message.title, message=mailing.message.body,
                              auth_user=settings.EMAIL_HOST_USER, recipient_list=client_list,
                              from_email=settings.DEFAULT_FROM_EMAIL)
                    log = Log.objects.create(status='Успешно', server_response='200')
                    log.save()
                except smtplib.SMTPException as err:
                    log = Log.objects.create(status='Ошибка', server_response=err)
                    log.save()
                except smtplib.SMTPDataError as err:
                    log = Log.objects.create(status='Ошибка', server_response=err)
                    log.save()
                except Exception as err:
                    log = Log.objects.create(status='Ошибка', server_response=err)
                    log.save()
