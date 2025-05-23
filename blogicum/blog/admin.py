from django.contrib import admin

from .models import (Category,
                     Location,
                     Post,
                     Comment,)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published',
        'created_at'

    )

    list_editable = (
        'is_published',
        'category',
        'pub_date'
    )

    search_fields = (
        'title',
    )

    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published'

    )

    list_editable = (
        'is_published',
        'slug'
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'post',
        'created_at',
        'author'
    )


admin.site.register(Location)
