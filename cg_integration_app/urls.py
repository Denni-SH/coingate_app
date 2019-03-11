"""cg_integration_app URL Configuration
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from .views import switch_language
urlpatterns = [
    path('admin/', admin.site.urls),
    path('switch_language/lang=<slug:lang>', switch_language, name='switch_lang'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    path('', include('apps.main.urls')),
)