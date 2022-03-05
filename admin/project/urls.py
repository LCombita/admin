from django.urls import path
from .views import ProyectoCreateView, ProyectoListView, ProyectoDeleteView, ProyectoUpdateView
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

project_patterns = ([
    #path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
    #path('num-esc/<int:pk>', NumeroEscrituraUpdateView.as_view(), name='numero-escritura'),
    path('pro-cre', ProyectoCreateView.as_view(), name='proyecto-create'),
    path('pro-list', ProyectoListView.as_view(), name='proyecto-list'),
    path('pro-upd/<int:pk>', ProyectoUpdateView.as_view(), name='proyecto-update'),
    path('pro-del/<int:pk>', ProyectoDeleteView.as_view(), name='proyecto-delete'),
    path('cli-list', ClienteListView.as_view(), name='cliente-list'),
    path('cli-cre', ClienteCreateView.as_view(), name='cliente-create'),
    path('cli-upd/<int:pk>', ClienteUpdateView.as_view(), name='cliente-update'),
    path('cli-del/<int:pk>', ClienteDeleteView.as_view(), name='cliente-delete'),
], 'project')