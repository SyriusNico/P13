from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    dictionnary = context['request'].GET.copy()
    for key, value in kwargs.items():
        dictionnary[key] = value
    for key in [key for key, value in dictionnary.items() if not value]:
        del dictionnary[key]
    return dictionnary.urlencode()