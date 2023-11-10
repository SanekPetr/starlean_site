from django.contrib import admin
from django.utils.html import format_html
from .models import Status
from .models import Product
from .models import Photo
from .models import Comment
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'gender', 'birthdate']
    list_filter = ['gender', 'birthdate']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'quantity', 'status', 'spent', 'pictures']
    list_filter = ['status', 'name']
    def spent(self, obj):
        return obj.price*obj.quantity
    
    def pictures(self, obj):
        pictures_tag = ''
        for photo in obj.photos.all():
            pictures_tag += f'<img src="{photo.image.url}" width="250px"><br>'
        return format_html(pictures_tag)
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display=['id', 'image', 'picture']
    def picture(self, obj):
        return format_html(f"<img src='{obj.image.url}' width='25%'>")
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']

# @admin.register(Clothes)
# class ClothesAdmin(admin.ModelAdmin):
#         list_display = ['id', 'name', 'price', 'quantity', 'status', 'spent', 'pictures']
#         list_filter = ['status', 'name']
#
#         def spent(self, obj):
#             return obj.price * obj.quantity