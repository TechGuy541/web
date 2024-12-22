from django import template

register = template.Library()

COMPATIBILITY_COLORS = {
    'Perfect': 'badge-success',
    'Playable': 'badge-warning',
    'Menu': 'bg-orange-400',
    'Boots': 'badge-error',
    'Nothing': 'badge-ghost',
}

RAM_COLORS = {
    '16GB': 'badge-success',
    '8GB': 'badge-success',
    '6GB': 'badge-warning',
    '4GB': 'bg-orange-400',
    '3GB': 'bg-error',
}

@register.filter
def compatibility_color(status):
    return COMPATIBILITY_COLORS.get(status, '')

@register.filter
def ram_color(memory):
    return RAM_COLORS.get(memory, '')