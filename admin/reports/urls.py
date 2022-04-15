from django.urls import path
from .views import ReportRepartosXOtorganteView, ReportRepartoTramitadorListView
from .views import ReportRepartosXAsistenteEscrituracionView


reports_patterns = ([
    path('rep-oto', ReportRepartosXOtorganteView.as_view(), name='repartos-otorgante'),
    path('rep-tra', ReportRepartoTramitadorListView.as_view(), name='repartos-tramitador'),
    path('rep-asi', ReportRepartosXAsistenteEscrituracionView.as_view(), name='repartos-asistente'),
    #path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
], 'reports')