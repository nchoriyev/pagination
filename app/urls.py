from django.urls import path
from .views import MainView, UserView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('users/', UserView.as_view(), name='users'),
]