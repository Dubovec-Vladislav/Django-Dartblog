from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('templatetags_templates/posts_tpl.html')
def show_posts(cnt=4):
    posts = cnt
    return {"posts": posts}


@register.inclusion_tag('templatetags_templates/stationary_post_tpl.html')
def get_stationary_post():
    posts = Post.objects.order_by('-views')[:1]
    return {"posts": posts}
