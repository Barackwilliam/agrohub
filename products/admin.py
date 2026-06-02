from django.contrib import admin
from .models import ProductCategory, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    fields = ('name', 'short_description', 'image', 'is_featured', 'is_active', 'order')
    show_change_link = True


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductInline]
    ordering = ('order',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
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
