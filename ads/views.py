from django.shortcuts import render

from .models import Ad


def GetAdsView(request):
    ads = Ad.objects.all()
    
    context = {
        'ads': ads,
    }

    return render(request, 'pages/ads_list.html', context)
