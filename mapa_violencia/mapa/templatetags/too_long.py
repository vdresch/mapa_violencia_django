from django import template

register = template.Library()


def too_long(i):
    print(i)
    print(len(i))
    if len(i) > 50:
        i = i[0:50] + '...'

    return i

register.simple_tag(too_long)