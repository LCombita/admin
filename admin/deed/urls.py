from django.urls import path
from .views import RepartoUpdateView, RepartoListView

deed_patterns = ([
    path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
    path('rep-list', RepartoListView.as_view(), name='reparto-list'),
], 'deed')