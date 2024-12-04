from django.contrib import admin
from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    search_fields = ['title', 'content']
    list_filter = ('author', 'category', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'created_at')
    search_fields = ['content', 'name']
    list_filter = ('created_at',)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
