from django import template
from ..models import PostQuestion


register = template.Library()


@register.simple_tag
def total_questions():
    return PostQuestion.created_on.count()
