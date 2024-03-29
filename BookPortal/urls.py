from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',include('BooksApp.urls')),
    path('',include('UserApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

admin.site.site_header = 'BookPortal'
admin.site.site_title = 'BookPortal-Administration'
admin.site.index_title = 'BookPortal-Administration'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
