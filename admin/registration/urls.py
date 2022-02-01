from django.urls import path
from .views import HomePageView, CreateGrantorView, DataGrantorView
from .views import GrantorListView, UpdateGrantorView


registration_patterns = ([
    path('', HomePageView.as_view(), name="home"),
    path('create-grantor', CreateGrantorView.as_view(), name="create-grantor"),
    path('update-grantor/<int:pk>/', UpdateGrantorView.as_view(), name="update-grantor"),
    path('data-grantor/<int:pk>/', DataGrantorView.as_view(), name="data-grantor"),
    path('grantor-list', GrantorListView.as_view(), name="grantor-list"),
    #path('thread/<int:pk>/add/', add_message, name="add"),
    #path('thread/start/<username>/', start_thread, name="start"),
], 'registration')