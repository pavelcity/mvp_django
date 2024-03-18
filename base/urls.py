from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.views.generic import TemplateView

urlpatterns = [
    path('suenter77/', admin.site.urls),
    path('', include('mvpcode.urls')),
    path('robots.txt', serve, {'document_root': settings.BASE_DIR, 'path': 'robots.txt'}, name='robots.txt'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





