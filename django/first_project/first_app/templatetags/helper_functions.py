from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='add_name')
@stringfilter
def add_my_name(value,param):
    return value+" "+param