from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f'/media/article/{val}'

    return '/media/utils/profile_nophoto.jpg'


@register.filter()
def mymedia(val):
    if val:
        return f'/media/users/{val}'

    return '/media/utils/profile_nophoto_50x50.jpg'
