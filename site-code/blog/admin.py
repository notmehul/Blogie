from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on') # displays properties
    list_filter = ("status",) #filter based on status
    search_fields = ['title', 'content'] # for the search bar
    prepopulated_fields = {'slug': ('title',)} # if someone forgets to fill the slug lol

admin.site.register(Post, PostAdmin)