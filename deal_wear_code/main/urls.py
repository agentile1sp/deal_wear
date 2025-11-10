from django.contrib import admin
from django.urls import path, include  # <--- importamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # <--- conectamos las rutas de la app "main"
]
