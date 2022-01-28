from django.urls import path
from .views import HomePageView, CreateGrantorView

registration_patterns = ([
    path('', HomePageView.as_view(), name="home"),
    path('create-grantor', CreateGrantorView.as_view(), name="create-grantor"),
    #path('thread/<int:pk>/', ThreadDetailView.as_view(), name="detail"),
    #path('thread/<int:pk>/add/', add_message, name="add"),
    #path('thread/start/<username>/', start_thread, name="start"),
], 'registration')