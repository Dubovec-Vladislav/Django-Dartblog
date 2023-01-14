from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('templatetags_templates/popular_posts_tpl.html')
def get_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('templatetags_templates/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}


@register.inclusion_tag('templatetags_templates/search_tpl.html')
def show_search_menu():
    pass


@register.inclusion_tag('templatetags_templates/email_tpl.html')
def show_email_menu():
    pass

# @register.filter()
