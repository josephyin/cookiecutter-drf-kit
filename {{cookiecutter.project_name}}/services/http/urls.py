from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.utils.translation import gettext, gettext_lazy as _
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.views.i18n import JavaScriptCatalog
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('services.http.v1.urls', namespace='v1')),
    path('i18n/', include('django.conf.urls.i18n')),
    # https://docs.djangoproject.com/en/dev/topics/i18n/translation/#note-on-performance
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('robots.txt', cache_page(60 * 60)(TemplateView.as_view(template_name='robots.txt', content_type='text/plain')))
]

# Vendor
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# if apps.is_installed('rosetta'):
#     urlpatterns += [path('rosetta/', include('rosetta.urls'))]

admin.site.site_header = _('app_name')
admin.site.site_title = _('app_name')
