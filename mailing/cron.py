from datetime import datetime, timedelta
import smtplib

import pytz
from django.conf import settings
from django.core.mail import send_mail

from client.models import Client
from mailing.models import Mailing, Log


# def calculate_next_send_time(frequency, last_send_time):
#     if frequency == Mailing.objects.filter(status=1):
#         return last_send_time + timedelta(days=1)
#     elif frequency == Mailing.objects.filter(status=2):
#         return last_send_time + timedelta(weeks=1)
#     elif frequency == Mailing.objects.filter(status=3):
#         return last_send_time + timedelta(days=30)


def my_scheduled_job():
    mailing_list = Mailing.objects.filter(status=2)
    tz = pytz.timezone('Europe/Moscow')
    for mailing in mailing_list:
        # next_send_time = calculate_next_send_time(mailing.frequency, mailing.mailing_time)
        now = datetime.now(tz)
        client_list = [client.contact_email for client in Client.objects.filter(is_active=True, user=mailing.user)]
        if mailing.mailing_time <= now:
            try:
                subj = mailing.message.title
                mess = mailing.message.body
                send_mail(subj, mess, settings.EMAIL_HOST_USER, client_list)
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
            mailing.status = 3
            mailing.save()
