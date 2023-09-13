from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'creation_date', 'is_published', 'owner')
    list_filter = ('title', 'content', 'creation_date', 'is_published', 'owner')
