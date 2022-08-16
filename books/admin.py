from django.contrib import admin
from books.models import Post,Category,Review,Contact

# Register your models here.

class PostAdmin(admin.TabularInline):
    model = Post
    prepopulated_fields = {'slug':('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name","image"]
    list_display_links = ["id","name"]
    inlines = [
        PostAdmin
    ]
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id","author","post","content","rating"]
    list_display_links = ["id","author","post","content","rating"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id","user","phone","email","desc","created"]
