from django.urls import path
from .views import HomePageView

registration_patterns = ([
    path('', HomePageView.as_view(), name="home"),
    #path('thread/<int:pk>/', ThreadDetailView.as_view(), name="detail"),
    #path('thread/<int:pk>/add/', add_message, name="add"),
    #path('thread/start/<username>/', start_thread, name="start"),
], 'registration')