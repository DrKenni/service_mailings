from django.conf import settings
from django.core.cache import cache

from blog.models import Article
from mailing.models import Mailing


def get_log_list(log_pk):
    if settings.CACHE_ENABLED:
        key = f'log_list_{log_pk}'
        log_list = cache.get(key)
        if log_list is None:
            log_list = Mailing.object.all(log__pk=log_pk)
            cache.set(key, log_list)
        else:
            log_list = Mailing.object.all(log__pk=log_pk)
        return log_list


def get_cache_for_article(article_pk):
    if settings.CACHE_ENABLED:
        key = f'article_list{article_pk}'
        article_list = cache.get(key)
        if article_list is None:
            article_list = Article.objects.filter(article__pk=article_pk)
            cache.set(key, article_list)
    else:
        article_list = Article.objects.filter(article__pk=article_pk)
    return article_list
