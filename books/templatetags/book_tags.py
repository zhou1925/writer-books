from django import template
from django.utils.safestring import mark_safe


from markdown_it import MarkdownIt


register = template.Library()

markdown = (MarkdownIt())

@register.filter
def markdownIt(text):
    return mark_safe(markdown.render(text))