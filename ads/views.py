from django.shortcuts import render
from .models import Ad


def GetAdsView(request):
    ads = Ad.objects.all()
    
    context = {
        'ads': ads,
    }

    return render(request, 'pages/ads_list.html', context)

def GetAdsCreate(request):
    return render(request, 'pages/ads_create.html')

def CreateAd(request):
    ad = Ad(
        title=request.POST['title'],
        description=request.POST['description'],
        complete_address=request.POST['complete_address'],
        photo1_url=request.POST['photo1_url'],
        photo2_url=request.POST['photo2_url'],
        phone=request.POST['phone'],
    )

    ad.save()

    ads = Ad.objects.all()
    
    context = {
        'ads': ads,
    }

    return render(request, 'pages/ads_list.html', context)

def ShowAdView(request):
    ad = Ad.objects.filter(id=request.GET['id'])[0]

    context = {
        'ad': ad,
    }

    return render(request, 'pages/ads_show.html', context)
