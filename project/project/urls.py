from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "A.M.I.T Administration"
admin.site.index_title = 'Feature Area'
admin.site.site_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)