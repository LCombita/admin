from django.contrib import admin
from django.urls import path, include
from registration.urls import registration_patterns

urlpatterns = [
    path('', include(registration_patterns)),
    path('admin/', admin.site.urls),
    #paths de Auth, estas para extender el sistema de registro de django
    #es decir, no se crearan vistas para iniciar o cerrar la sesión, solo los Templates
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/', include('registration.urls')),
]
