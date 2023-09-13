from django.contrib import admin

from mailing.models import Message, Mailing, Log


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'status', 'frequency', 'message', 'user')
    list_filter = ('mailing_time', 'status', 'frequency', 'message', 'user')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('date_attempts', 'status', 'server_response')
    list_filter = ('date_attempts', 'status', 'server_response')
