from django import template

register = template.Library()


@register.filter
def get_comments_count(comments, post):
    return comments.filter(post=post).count()
