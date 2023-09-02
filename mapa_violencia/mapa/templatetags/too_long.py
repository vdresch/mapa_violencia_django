from django import template

register = template.Library()


def too_long(i):
    if len(i) > 40:
        i = i[0:40] + '...'

    return i

register.simple_tag(too_long)