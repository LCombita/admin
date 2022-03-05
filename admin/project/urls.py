from django.urls import path
from .views import ProyectoCreateView, ProyectoListView
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView

project_patterns = ([
    #path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
    #path('num-esc/<int:pk>', NumeroEscrituraUpdateView.as_view(), name='numero-escritura'),
    path('pro-cre', ProyectoCreateView.as_view(), name='proyecto-create'),
    path('pro-list', ProyectoListView.as_view(), name='proyecto-list'),
    path('cli-list', ClienteListView.as_view(), name='cliente-list'),
    path('cli-cre', ClienteCreateView.as_view(), name='cliente-create'),
    path('cli-upd/<int:pk>', ClienteUpdateView.as_view(), name='cliente-update'),
], 'project')