from django import template

register = template.Library()


def too_long_mobile(i):
    print(i)
    print(len(i))
    if len(i) > 35:
        i = i[0:35] + '...'

    return i

register.simple_tag(too_long_mobile)