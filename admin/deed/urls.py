from django.urls import path
from .views import RepartoUpdateView

deed_patterns = ([
    path('rep-upd/<int:pk>', RepartoUpdateView.as_view(), name='reparto-update'),
], 'deed')