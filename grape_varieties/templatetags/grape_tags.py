from django import template
import grape_varieties.views as views
from grape_varieties.models import Category, TagGrape

register = template.Library()


@register.inclusion_tag('grape_varieties/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('grape_varieties/list_tags.html')
def show_all_tags():
    return {'tags': TagGrape.objects.all()}

