from django import template
from django.db.models import Count, F
from blog.models import Category

register = template.Library()


@register.inclusion_tag('templatetags_templates/menu_tpl.html')
def show_menu(menu_class='menu'):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count("get_category", filter=F("get_category__is_published"))).\
        filter(cnt__gt=0)
    return {'categories': categories, 'menu_class': menu_class}
