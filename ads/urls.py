from django.urls import path

from .views import GetAdsView, GetAdsCreate, CreateAd, ShowAdView

urlpatterns = [
    path('list/', GetAdsView, name='list'),
    path('show/', ShowAdView, name='show'),
    path('create/', GetAdsCreate, name='create'),
    path('create/createAd', CreateAd, name='createAd'),
]