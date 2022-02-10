from django.template import Library

register = Library()


@register.filter
def mm(value):
    return value.upper()


# register.filter(mm)


@register.filter
def cut(value, arg):
    return value.replace(arg, '')
