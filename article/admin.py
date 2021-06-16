from django.contrib import admin

# Register your models here.
from .models import About, Article,Category,Comment

#admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article","comment_name"]
    search_fields = ["comment_name"]

@admin.register(About)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","created_date"]
    list_display_links = ["title"]
    search_fields = ["title"]
    list_filter = ["created_date"]

    class Meta:
        model = Article