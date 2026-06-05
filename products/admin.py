from django.contrib import admin
from .models import ProductCategory, Product
from .forms import ProductCategoryForm,ProductForm


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    fields = ('name', 'short_description', 'image', 'is_featured', 'is_active', 'order')
    show_change_link = True


# @admin.register(ProductCategory)
# class ProductCategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'icon', 'order', 'is_active')
#     list_editable = ('order', 'is_active')
#     prepopulated_fields = {'slug': ('name',)}
#     inlines = [ProductInline]
#     ordering = ('order',)



class ProductCategoryAdmin(admin.ModelAdmin):
    form = ProductCategoryForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'cff49d484a4e0a5d423f', 
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;">')
        return "No Image"

    image_preview.short_description = 'Image Preview'

    list_display = ('name', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductInline]
    ordering = ('order',)

admin.site.register(ProductCategory, ProductCategoryAdmin)


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'is_featured', 'is_active', 'order')
#     list_editable = ('is_featured', 'is_active', 'order')
#     list_filter = ('category', 'is_featured', 'is_active')
#     search_fields = ('name', 'description')
#     prepopulated_fields = {'slug': ('name',)}
#     fieldsets = (
#         ('Basic Info', {
#             'fields': ('category', 'name', 'slug', 'short_description', 'description', 'image'),
#         }),
#         ('Product Details', {
#             'fields': ('origin', 'available_seasons', 'minimum_order', 'packaging', 'certifications'),
#         }),
#         ('Display Options', {
#             'fields': ('is_featured', 'is_active', 'order'),
#         }),
#     )





class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'cff49d484a4e0a5d423f', 
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;">')
        return "No Image"

    image_preview.short_description = 'Image Preview'

    list_display = ('name', 'category', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Info', {
            'fields': ('category', 'name', 'slug', 'short_description', 'description', 'image'),
        }),
        ('Product Details', {
            'fields': ('origin', 'available_seasons', 'minimum_order', 'packaging', 'certifications'),
        }),
        ('Display Options', {
            'fields': ('is_featured', 'is_active', 'order'),
        }),
    ) 
admin.site.register(Product, ProductAdmin)
