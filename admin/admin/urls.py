from django.contrib import admin
from django.urls import path, include
from registration.urls import registration_patterns
from deed.urls import deed_patterns
from project.urls import project_patterns
from stage.urls import stage_patterns

urlpatterns = [
    path('', include(registration_patterns)),
    path('admin/', admin.site.urls),
    #path de deed
    path('deed/', include(deed_patterns)),
    #path de project
    path('project/', include(project_patterns)),
    #path de stage
    path('stage/', include(stage_patterns)),
    
    #paths de Auth, estas para extender el sistema de registro de django
    #es decir, no se crearan vistas para iniciar o cerrar la sesión, solo los Templates
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/', include('registration.urls')),
]
