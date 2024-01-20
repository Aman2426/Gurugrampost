from django.contrib import admin
from.models import Article,Category,Comment,Vote

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Vote)



# class ArticleInline(admin.TabularInline):
#     model = Article
#     extra = 0

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [ArticleInline]

# admin.site.register(Author,AuthorAdmin)