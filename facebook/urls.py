from django.urls import path
from .views import facebook_post_view,home

urlpatterns = [
    path('', home, name='home'),
    path('facebook/', facebook_post_view, name='facebook_post'),
]
