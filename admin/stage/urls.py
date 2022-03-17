from django.urls import path
from .views import EtapaCreateView, EtapaListView, EtapaDeleteView, EtapaUpdateView
from .views import RepartoEtapaUpdateView


stage_patterns = ([
    #path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
    #path('num-esc/<int:pk>', NumeroEscrituraUpdateView.as_view(), name='numero-escritura'),
    path('eta-cre', EtapaCreateView.as_view(), name='etapa-create'),
    path('eta-list', EtapaListView.as_view(), name='etapa-list'),
    path('eta-upd/<int:pk>', EtapaUpdateView.as_view(), name='etapa-update'),
    path('eta-del/<int:pk>', EtapaDeleteView.as_view(), name='etapa-delete'),
    #REPARTO ETAPA
    path('ret-upd/<int:pk>', RepartoEtapaUpdateView.as_view(), name='repartoetapa-update'),
], 'stage')