from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "East Africa AgroHub Admin"
admin.site.site_title = "AgroHub Admin Portal"
admin.site.index_title = "Welcome to AgroHub Management"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('products/', include('products.urls')),
    path('inquiries/', include('inquiries.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
