from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from registration.urls import registration_patterns
from deed.urls import deed_patterns
from project.urls import project_patterns
from stage.urls import stage_patterns
from reports.urls import reports_patterns

urlpatterns = [
    path('', include(registration_patterns)),
    path('admin/', admin.site.urls),
    #path de deed
    path('deed/', include(deed_patterns)),
    #path de project
    path('project/', include(project_patterns)),
    #path de stage
    path('stage/', include(stage_patterns)),
    #path de reports
    path('reports/', include(reports_patterns)),
    
    #paths de Auth, estas para extender el sistema de registro de django
    #es decir, no se crearan vistas para iniciar o cerrar la sesión, solo los Templates
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/', include('registration.urls')),
]

#almacenamiento de imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
