from django.urls import path, include
from gameclub.views.index.index import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index html'),
    path('gameclub/', include('gameclub.urls.gameclub.index'),name = 'gameclub')
]
