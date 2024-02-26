from django.contrib import admin
from .models import Post
from .models import Post1
from .models import Post2

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'body']
    list_filter = ['date']
    search_fields = ['title']
admin.site.register(Post, PostAdmin)
admin.site.register(Post1, PostAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'body', 'image']
    list_filter = ['date']
    search_fields = ['title']
admin.site.register(Post2, PostAdmin)
