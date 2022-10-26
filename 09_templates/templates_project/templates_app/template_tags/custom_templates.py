from django import template

register = template.Library()

# you can also use generators
# @register.filter(name='cut)
def cut(value, arg):
    """
    this cuts out all values of arg from the string
    """
    return value.replace(arg,'')

# you register your template filter, you pass in as a string what 
# you want to call the filter
register.filter('cut',cut)