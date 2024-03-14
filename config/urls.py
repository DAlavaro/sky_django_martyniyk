from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('app.catalog.urls', 'catalog'))),
    path('admin/', admin.site.urls),
]
