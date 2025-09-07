"""Over all project URL of all application."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donations/', include('donations.urls')),
    path('', include('donations.urls')),
]
