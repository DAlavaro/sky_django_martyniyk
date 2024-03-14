from django.urls import path
from app.catalog.views import index, contacts

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
]
