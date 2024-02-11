from django.contrib import admin
from.models import Article,Category,Comment,Vote,Section,Bookmark

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Section)
admin.site.register(Bookmark)



# class ArticleInline(admin.TabularInline):
#     model = Article
#     extra = 0

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [ArticleInline]

# admin.site.register(Author,AuthorAdmin)