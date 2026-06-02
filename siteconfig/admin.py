from django.contrib import admin
from .models import SiteSettings, HeroSlide, WhyChooseUs, CoreValue, SocialLink, Statistic


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('🏢 Company Identity', {
            'fields': ('company_name', 'tagline', 'logo', 'favicon'),
        }),
        ('📖 About Section', {
            'fields': ('about_title', 'about_text', 'about_image'),
        }),
        ('🎯 Vision & Mission', {
            'fields': ('vision', 'mission'),
        }),
        ('📞 Contact Information', {
            'fields': ('phone', 'email', 'location', 'google_maps_embed'),
        }),
        ('🔍 SEO Settings', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    ordering = ('order',)


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'is_active')
    list_editable = ('is_active',)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('number', 'label', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)
