from jinja2 import Markup
from coffin import template
register = template.Library()

from djangospot.utils.json import dumps

@register.filter()
def json(value):
    if not value:
        return 'null'
    return Markup(dumps(value))