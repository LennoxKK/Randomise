from django import template
register = template.Library()

@register.simple_tag
def setvar(val=None):
    return val

register.simple_tag(lambda x:x - 1, name = "minusone")


@register.simple_tag()
def some_function(value):
    return value -2