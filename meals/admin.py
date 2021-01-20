from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Meals, Category

# Register your models here.
class MealsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Meals,MealsAdmin)
admin.site.register(Category)