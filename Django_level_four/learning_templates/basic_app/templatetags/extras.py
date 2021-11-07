""" 
This file is used to create a customized filters in django
"""

from django import template

register = template.Library()



@register.filter(name="cut")
def cut(value, arg):
    """
    This cuts out the all args from the string!
    """
    return value.replace(arg, '')

# register.filter('cut', cut)
