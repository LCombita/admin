from django.urls import path
from .views import RepartoUpdateView, RepartoListView, NumeroEscrituraUpdateView
from .views import RepartoCreateView, RepartoInmuebleEditView, RepartoDetailView
from .views import ActoCreateView, ActoUpdateView, ActoListView, ActoDeleteView

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
], 'deed')