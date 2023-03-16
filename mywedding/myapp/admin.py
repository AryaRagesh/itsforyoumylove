from django.contrib import admin
from .models import Year,Product
# Register your models here.

class YearAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Year,YearAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','image']
   # list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product,ProductAdmin)
