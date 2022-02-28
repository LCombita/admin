from django.urls import path
from .views import RepartoUpdateView, RepartoListView, NumeroEscrituraUpdateView

deed_patterns = ([
    path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
    path('num-esc/<int:pk>', NumeroEscrituraUpdateView.as_view(), name='numero-escritura'),
    path('rep-list', RepartoListView.as_view(), name='reparto-list'),
], 'deed')