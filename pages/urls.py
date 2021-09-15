from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.homepage, name="homepage"),
    #path('aboutus', views.aboutUs, name="aboutUs"),
    #path('informations', views.infos, name="infos"),
]

    

    