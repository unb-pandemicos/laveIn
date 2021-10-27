from django.http import HttpResponse
from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
def homepage(request):
    return render(request, 'pages/homepage.html' )
=======
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
>>>>>>> eac3cf274ba0aa8ca35eba82649b6d7e7c5f5460
