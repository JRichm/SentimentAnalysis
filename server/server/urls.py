from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView  # Add this import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/', include('api.urls')),
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)