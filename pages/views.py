from django.http import HttpResponse
from django.shortcuts import render

from ads.models import Ad

def homepage(request):
    print('// -=-=-=- TRY GEY ADS -=-=-=-=-')
    # Get all ads on database
    ads = Ad.objects.order_by('created_at')[:3]

    print('// -=-=-=- GET ADS SUCESSFULLY -=-=-=-=-')

    context = {
        'ads': ads,
    }

    return render(request, 'pages/homepage.html', context)
