from .models import SiteSettings, SocialLink


def site_settings(request):
    settings = SiteSettings.get_settings()
    social_links = SocialLink.objects.filter(is_active=True)
    return {
        'site_settings': settings,
        'social_links': social_links,
    }
