from django import template

register = template.Library()


@register.filter()
def mymedia_blog(val):
    if val:
        return f'/media/article/{val}'

    return '/media/utils/profile_nophoto.jpg'


@register.filter()
def mymedia_user(val):
    if val:
        return f'/media/users/{val}'

    return '/media/utils/profile_nophoto_50x50.jpg'


@register.filter()
def limit_symbols(text):
    if text is None:
        return 'Без описания'
    elif len(text) > 50:
        return f'{text[:50]}...'
    else:
        return text
