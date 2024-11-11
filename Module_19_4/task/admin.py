from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    ordering = ('-published_date',)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    search_fields = ('author', 'text')
