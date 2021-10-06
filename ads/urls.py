from django.urls import path

from .views import GetAdsView

urlpatterns = [
    path('list/', GetAdsView, name='list'),
]