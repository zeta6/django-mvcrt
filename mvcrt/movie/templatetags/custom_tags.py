from django import template

register = template.Library()

@register.simple_tag
def number_plus_one(value):
    number = int(value) + 1
    return number
    