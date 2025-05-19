from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date', 'approved')
    list_filter = ('approved', 'created_date')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)