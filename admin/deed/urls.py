from django.urls import path
from .views import RepartoUpdateView, RepartoListView, NumeroEscrituraUpdateView
from .views import RepartoCreateView, RepartoInmuebleEditView, RepartoDetailView
from .views import ActoCreateView, ActoUpdateView, ActoListView, ActoDeleteView
from .views import RepartoOtorganteEditView, RepartoEtapasEditView

deed_patterns = ([
    path('rep-cre', RepartoCreateView.as_view(), name='reparto-create'),
    path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
    path('num-esc/<int:pk>', NumeroEscrituraUpdateView.as_view(), name='numero-escritura'),
    path('rep-det/<int:pk>', RepartoDetailView.as_view(), name='reparto-detail'),
    path('rep-list', RepartoListView.as_view(), name='reparto-list'),
    #ACTOS JURIDICOS
    path('act-cre', ActoCreateView.as_view(), name='acto-create'),
    path('act-upd/<int:pk>', ActoUpdateView.as_view(), name='acto-update'),
    path('act-del/<int:pk>', ActoDeleteView.as_view(), name='acto-delete'),
    path('act-list', ActoListView.as_view(), name='acto-list'),
    #INMUEBLES
    path('rep-inm/<int:pk>', RepartoInmuebleEditView.as_view(), name='reparto-inmueble-edit'),
    #OTORGANTES
    path('rep-oto/<int:pk>', RepartoOtorganteEditView.as_view(), name='reparto-otorgante-edit'),
    #ETAPAS
    path('rep-eta/<int:pk>', RepartoEtapasEditView.as_view(), name='reparto-etapas-edit'),
], 'deed')