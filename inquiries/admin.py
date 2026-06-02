from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'company', 'country', 'product_interest', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'country')
    search_fields = ('full_name', 'email', 'company', 'message')
    list_editable = ('status',)
    readonly_fields = ('full_name', 'email', 'phone', 'company', 'country', 'product_interest', 'message', 'created_at')
    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'email', 'phone', 'company', 'country'),
        }),
        ('Inquiry Details', {
            'fields': ('product_interest', 'message', 'created_at'),
        }),
        ('Management', {
            'fields': ('status', 'notes'),
        }),
    )

    def has_add_permission(self, request):
        return False
