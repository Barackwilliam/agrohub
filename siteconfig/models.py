from django.db import models


class SiteSettings(models.Model):
    """Global site settings - editable from admin"""
    # Company Info
    company_name = models.CharField(max_length=200, default="East Africa AgroHub Export Ltd")
    tagline = models.CharField(max_length=300, default="From East Africa to Global Markets")
    logo = models.ImageField(upload_to='site/', null=True, blank=True)
    favicon = models.ImageField(upload_to='site/', null=True, blank=True)

    # About
    about_title = models.CharField(max_length=200, default="About Us")
    about_text = models.TextField(default="East Africa AgroHub Export Ltd is a Tanzania-based agricultural export company...")
    about_image = models.ImageField(upload_to='about/', null=True, blank=True)

    # Vision & Mission
    vision = models.TextField(default="To become one of Africa's leading and most trusted agricultural export companies connecting local producers to international markets.")
    mission = models.TextField(default="To deliver premium agricultural products with integrity, efficiency, and international quality standards while empowering local agricultural value chains.")

    # Contact
    phone = models.CharField(max_length=50, default="+255 685 047 428")
    email = models.EmailField(default="export@eastafricaagrohub.co.tz")
    location = models.CharField(max_length=300, default="Dar es Salaam, Tanzania")
    google_maps_embed = models.TextField(blank=True, null=True)

    # SEO
    meta_description = models.TextField(max_length=300, default="East Africa AgroHub Export Ltd - Premium agricultural exports from Tanzania to global markets.")
    meta_keywords = models.CharField(max_length=500, default="agricultural export, Tanzania, East Africa, grains, horticulture, meat, seafood")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class HeroSlide(models.Model):
    """Hero section slides"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400, blank=True)
    cta_text = models.CharField(max_length=100, default="Explore Products")
    cta_link = models.CharField(max_length=200, default="/products/")
    background_image = models.ImageField(upload_to='hero/', null=True, blank=True)
    background_overlay_color = models.CharField(max_length=20, default="rgba(0,0,0,0.55)")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    """Why Choose Us section items"""
    icon = models.CharField(max_length=100, default="fas fa-check-circle", help_text="FontAwesome icon class e.g. fas fa-seedling")
    title = models.CharField(max_length=150)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Why Choose Us Item"
        verbose_name_plural = "Why Choose Us Items"

    def __str__(self):
        return self.title


class CoreValue(models.Model):
    """Core Values"""
    icon = models.CharField(max_length=100, default="fas fa-star")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Core Value"
        verbose_name_plural = "Core Values"

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    """Social media links"""
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter/X'),
        ('youtube', 'YouTube'),
        ('whatsapp', 'WhatsApp'),
        ('tiktok', 'TikTok'),
    ]
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self):
        return self.get_platform_display()

    def get_icon(self):
        icons = {
            'facebook': 'fab fa-facebook-f',
            'instagram': 'fab fa-instagram',
            'linkedin': 'fab fa-linkedin-in',
            'twitter': 'fab fa-x-twitter',
            'youtube': 'fab fa-youtube',
            'whatsapp': 'fab fa-whatsapp',
            'tiktok': 'fab fa-tiktok',
        }
        return icons.get(self.platform, 'fas fa-link')


class Statistic(models.Model):
    """Stats shown on homepage e.g. 500+ Farmers, 20+ Countries"""
    icon = models.CharField(max_length=100, default="fas fa-chart-line")
    number = models.CharField(max_length=50, help_text="e.g. 500+")
    label = models.CharField(max_length=150)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return f"{self.number} {self.label}"
