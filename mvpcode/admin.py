from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short', 'get_html_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title', 'short',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    readonly_fields = ('time_create', 'time_update')  # Добавьте это, чтобы сделать эти поля только для чтения
    prepopulated_fields = {'slug': ('title', )}
    save_on_top = True

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.cover_photo.url}' width=120>")

    get_html_photo.short_description = 'Картинка'


class CategoryarticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name', )}
    save_on_top = True




admin.site.register(Article, ArticleAdmin)
admin.site.register(Categoryarticle, CategoryarticleAdmin)