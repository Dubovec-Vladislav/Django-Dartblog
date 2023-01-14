from django.contrib import admin
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from django.utils.safestring import mark_safe


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

    list_display = ("id", "title", "slug")


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

    list_display = ("id", "title", "slug")


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

    form = PostAdminForm
    save_as = True
    save_on_top = True

    list_display = ("id", "title", "slug", "category", "created_at", "views", "get_photo")
    list_display_links = ("id", "title")
    search_fields = ("title", )
    list_filter = ("category", "tags", )

    readonly_fields = ("get_photo", "views", "created_at")
    fields = ("title", "slug", "author", "category", "tags",
              "content", "photo", "get_photo", "views", "created_at")

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50">')
        return 'Фото не установлено'

    get_photo.short_description = "Фото"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
