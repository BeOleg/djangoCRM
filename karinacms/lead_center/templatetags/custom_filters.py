from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='form_display')
@stringfilter
def form_display(value, delimeter):
    words = value.split(delimeter)
    output = value.replace(delimeter, ' ')
    return output[0].upper() + output[1:]