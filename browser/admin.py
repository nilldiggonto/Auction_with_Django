from django.contrib import admin
from .models import Product,Product_price,Category_post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__','title','timestamp','price']
    list_display_links = ['title','price']
    
    search_fields =['title','content']

    class Meta:
        model = Product


class BidAdmin(admin.ModelAdmin):
    list_display = ['__str__','product_title','timestamp','current_price']
    list_display_links = ['product_title','current_price']
    
    search_fields =['product_title','user']

    class Meta:
        model = Product_price

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__','c_title','created_at','updated_at']
    list_display_links = ['c_title',]
    
    search_fields =['c_title']

    class Meta:
        model = Category_post



admin.site.register(Product,PostAdmin)
admin.site.register(Product_price,BidAdmin)
admin.site.register(Category_post,CategoryAdmin)