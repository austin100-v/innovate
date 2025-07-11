from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', include('services.urls')),
    path('courses/', include('courses.urls')),
    path('users/', include('users.urls')),
    path('startups/', include('startups.urls')),
    path('custom_admin/', include('custom_admin.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
