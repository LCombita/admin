from django.urls import path
from .views import RepartoUpdateView, RepartoListView, NumeroEscrituraUpdateView
from .views import RepartoCreateView

deed_patterns = ([
    path('rep-cre', RepartoCreateView.as_view(), name='reparto-create'),
    path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
    path('num-esc/<int:pk>', NumeroEscrituraUpdateView.as_view(), name='numero-escritura'),
    path('rep-list', RepartoListView.as_view(), name='reparto-list'),
], 'deed')