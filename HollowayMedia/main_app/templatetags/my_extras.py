from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    this removes all instances of arg from a string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
