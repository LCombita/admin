from django.urls import path
from .views import EtapaCreateView, EtapaListView, EtapaDeleteView, EtapaUpdateView
from .views import RepartoEtapaUpdateView, RevisionRepartoEtapaEditView
from .views import ImpuestoRepartoEtapaEditView, RepartoEtapaDetailView, ObservacionCreateView, ObservacionCreate2View


stage_patterns = ([
    path('eta-cre', EtapaCreateView.as_view(), name='etapa-create'),
    path('eta-list', EtapaListView.as_view(), name='etapa-list'),
    path('eta-upd/<int:pk>', EtapaUpdateView.as_view(), name='etapa-update'),
    path('eta-del/<int:pk>', EtapaDeleteView.as_view(), name='etapa-delete'),
    #REPARTO ETAPA
    path('ret-upd/<int:pk>', RepartoEtapaUpdateView.as_view(), name='repartoetapa-update'),
    path('ret-det/<int:pk>', RepartoEtapaDetailView.as_view(), name='repartoetapa-detail'),
    #OBSERVACIONES
    path('ret-obs/<int:id>', ObservacionCreateView.as_view(), name='repartoetapa-observaciones'),
    path('ret-obs2/<int:id>', ObservacionCreate2View.as_view(), name='repartoetapa-observaciones2'),
    #REVISION
    path('ret-rev/<int:pk>', RevisionRepartoEtapaEditView.as_view(), name='repartoetapa-revision'),
    #IMPUESTO
    path('ret-imp/<int:pk>', ImpuestoRepartoEtapaEditView.as_view(), name='repartoetapa-impuesto'),
], 'stage')