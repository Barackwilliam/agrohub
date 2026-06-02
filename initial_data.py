"""
East Africa AgroHub - Initial Data Setup Script
Run: python manage.py shell < initial_data.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrohub.settings')
django.setup()

from siteconfig.models import SiteSettings, HeroSlide, WhyChooseUs, CoreValue, SocialLink, Statistic
from products.models import ProductCategory, Product

print("Setting up initial data...")

# --- Site Settings ---
settings, _ = SiteSettings.objects.get_or_create(pk=1)
settings.company_name = "East Africa AgroHub Export Ltd"
settings.tagline = "From East Africa to Global Markets"
settings.about_title = "About Us"
settings.about_text = """East Africa AgroHub Export Ltd is a Tanzania-based agricultural export company specializing in the sourcing, processing, packaging, and international supply of premium agricultural commodities.

We connect East African farmers and producers to global buyers through reliable export solutions, quality assurance, and professional trade services. Our company focuses on delivering high-quality grains, horticultural products, dry agricultural commodities, meat products, and seafood to international markets including Asia, the Middle East, and Europe.

With a strong commitment to quality, transparency, and long-term partnerships, we aim to position East African agriculture competitively in global markets."""
settings.vision = "To become one of Africa's leading and most trusted agricultural export companies connecting local producers to international markets."
settings.mission = "To deliver premium agricultural products with integrity, efficiency, and international quality standards while empowering local agricultural value chains."
settings.phone = "+255 685 047 428"
settings.email = "export@eastafricaagrohub.co.tz"
settings.location = "Dar es Salaam, Tanzania"
settings.meta_description = "East Africa AgroHub Export Ltd - Premium agricultural exports from Tanzania to global markets including Asia, Middle East and Europe."
settings.save()
print("✅ Site settings saved.")

# --- Hero Slides ---
HeroSlide.objects.all().delete()
HeroSlide.objects.create(
    title="Premium Agricultural Products from East Africa",
    subtitle="Connecting East African farmers to global buyers through reliable sourcing, quality assurance, and professional export solutions.",
    cta_text="Explore Products",
    cta_link="/products/",
    order=1
)
print("✅ Hero slides created.")

# --- Statistics ---
Statistic.objects.all().delete()
stats = [
    ("fas fa-tractor", "500+", "Farmer Partners"),
    ("fas fa-globe", "20+", "Export Countries"),
    ("fas fa-seedling", "15+", "Product Types"),
    ("fas fa-certificate", "100%", "Quality Assured"),
]
for i, (icon, number, label) in enumerate(stats):
    Statistic.objects.create(icon=icon, number=number, label=label, order=i)
print("✅ Statistics created.")

# --- Why Choose Us ---
WhyChooseUs.objects.all().delete()
why_items = [
    ("fas fa-network-wired", "Reliable Sourcing Network", "Direct partnerships with hundreds of farmers across Tanzania and East Africa, ensuring consistent supply year-round."),
    ("fas fa-certificate", "International Export Standards", "All products are processed and packaged to meet ISO, HACCP, and importing country requirements."),
    ("fas fa-tags", "Competitive Pricing", "Our direct farmer relationships eliminate unnecessary middlemen, giving you the best prices in the market."),
    ("fas fa-truck", "Professional Logistics Support", "End-to-end export management including documentation, customs clearance, and freight coordination."),
    ("fas fa-bolt", "Fast Communication", "Dedicated export managers available via WhatsApp, email, and phone for quick responses to all inquiries."),
    ("fas fa-shield-alt", "Quality Assurance Procedures", "Multi-stage quality inspection from farm to shipment, with laboratory testing available on request."),
]
for i, (icon, title, desc) in enumerate(why_items):
    WhyChooseUs.objects.create(icon=icon, title=title, description=desc, order=i)
print("✅ Why Choose Us items created.")

# --- Core Values ---
CoreValue.objects.all().delete()
values = [
    ("fas fa-star", "Quality Excellence", "We maintain the highest standards in every product we export, from sourcing to delivery."),
    ("fas fa-handshake", "Integrity & Transparency", "Honest pricing, clear communication, and no hidden costs in all our business dealings."),
    ("fas fa-check-double", "Reliability", "Consistent supply, on-time delivery, and dependable service you can count on."),
    ("fas fa-smile", "Customer Satisfaction", "Your success is our success. We go the extra mile to exceed your expectations."),
    ("fas fa-leaf", "Sustainable Trade", "Supporting sustainable farming practices and fair compensation for East African farmers."),
    ("fas fa-lightbulb", "Innovation & Growth", "Continuously improving our processes and expanding our product range to serve you better."),
]
for i, (icon, title, desc) in enumerate(values):
    CoreValue.objects.create(icon=icon, title=title, description=desc, order=i)
print("✅ Core values created.")

# --- Social Links ---
SocialLink.objects.all().delete()
SocialLink.objects.create(platform='whatsapp', url='https://wa.me/255685047428')
SocialLink.objects.create(platform='facebook', url='https://facebook.com/EastAfricaAgroHub')
SocialLink.objects.create(platform='instagram', url='https://instagram.com/EastAfricaAgroHub')
SocialLink.objects.create(platform='linkedin', url='https://linkedin.com/company/EastAfricaAgroHub')
print("✅ Social links created.")

# --- Product Categories & Products ---
ProductCategory.objects.all().delete()

# Grains & Cereals
grains = ProductCategory.objects.create(
    name="Grains & Cereals", slug="grains-cereals",
    icon="fas fa-wheat-awn",
    description="Premium quality grains and cereals sourced from Tanzania's highland farms.",
    order=1
)
for name, desc in [
    ("Maize", "Premium white and yellow maize. Year-round availability from Tanzania's highland regions."),
    ("Rice", "Long-grain and short-grain rice varieties. Processed to export-grade quality."),
    ("Sorghum", "Red and white sorghum for food processing and brewing industries."),
    ("Millet", "Finger millet and pearl millet. Rich in nutrients, popular in Asia and Middle East."),
    ("Beans", "Various bean varieties including kidney beans, black-eyed peas, and green grams."),
]:
    Product.objects.create(category=grains, name=name, short_description=desc,
        origin="Tanzania, East Africa", minimum_order="5 Metric Tons",
        packaging="25kg PP bags or 50kg jute bags", is_featured=True, order=1)

# Horticulture
hort = ProductCategory.objects.create(
    name="Horticulture Products", slug="horticulture-products",
    icon="fas fa-apple-alt",
    description="Fresh fruits and vegetables from East Africa's fertile farms.",
    order=2
)
for name, desc in [
    ("Avocado", "Hass and Fuerte avocados. Export-grade quality, air and sea freight available."),
    ("Mango", "Kent, Tommy Atkins, and local varieties. Sweet, ripe, and export-ready."),
    ("Vegetables", "Mixed fresh vegetables including okra, African eggplant, and leafy greens."),
    ("Fresh Fruits", "Seasonal tropical fruits including passion fruit, papaya, and pineapple."),
]:
    Product.objects.create(category=hort, name=name, short_description=desc,
        origin="Tanzania, East Africa", minimum_order="2 Metric Tons",
        available_seasons="March–September", is_featured=True, order=2)

# Dry Agricultural
dry = ProductCategory.objects.create(
    name="Dry Agricultural Products", slug="dry-agricultural-products",
    icon="fas fa-pepper-hot",
    description="Premium dried spices, seeds, and pulses.",
    order=3
)
for name, desc in [
    ("Dry Red Chili", "Sun-dried red chili peppers with high capsaicin content. Whole and crushed."),
    ("Sesame Seeds", "White and brown sesame seeds. High oil content, HACCP certified."),
    ("Spices", "Cinnamon, cardamom, cloves, and black pepper from Tanzania's spice farms."),
    ("Pulses", "Lentils, chickpeas, and various dried legumes for food processing markets."),
]:
    Product.objects.create(category=dry, name=name, short_description=desc,
        origin="Tanzania, East Africa", minimum_order="1 Metric Ton",
        packaging="10kg or 25kg PP bags", is_featured=True, order=3)

# Meat & Seafood
meat = ProductCategory.objects.create(
    name="Meat & Seafood", slug="meat-seafood",
    icon="fas fa-fish",
    description="Halal-certified meat and fresh seafood from East Africa.",
    order=4
)
for name, desc in [
    ("Beef Products", "Halal-certified premium beef cuts. Chilled and frozen options available."),
    ("Goat Meat", "Fresh and frozen halal goat meat. Popular in Middle East and Asian markets."),
    ("Fish & Seafood", "Nile perch, tilapia, and Indian Ocean seafood. Fresh and frozen export."),
]:
    Product.objects.create(category=meat, name=name, short_description=desc,
        origin="Tanzania, East Africa", minimum_order="500 Kg",
        certifications="Halal Certified, TFDA", is_featured=False, order=4)

print("✅ Products and categories created.")
print("\n🎉 Initial data setup complete!")
print("You can now run: python manage.py runserver")
