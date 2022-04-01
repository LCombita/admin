from django.urls import path
from .views import ReportRepartosXOtorganteView


reports_patterns = ([
    path('rep-oto', ReportRepartosXOtorganteView.as_view(), name='repartos-otorgante'),
    #path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
], 'reports')