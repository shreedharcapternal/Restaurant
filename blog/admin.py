from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Category,Post,Comment
# Register your models here.
class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    list_display = ['title','author','category','created']
    search_fields = ['title']
    list_filter = ['category','tags']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
