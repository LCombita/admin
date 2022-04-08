from django.urls import path
from .views import ReportRepartosXOtorganteView, ReportRepartoTramitadorListView


reports_patterns = ([
    path('rep-oto', ReportRepartosXOtorganteView.as_view(), name='repartos-otorgante'),
    path('rep-tra', ReportRepartoTramitadorListView.as_view(), name='repartos-tramitador'),
    #path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
], 'reports')