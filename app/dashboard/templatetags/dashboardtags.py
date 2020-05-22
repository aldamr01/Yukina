from django import template

register = template.Library() 


@register.filter(name='percentage')
def percentage(value):
    return float(value) / float(300) * float(100)