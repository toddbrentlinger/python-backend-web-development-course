from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    # feature1 = Feature('Fast', 'Our service is very quick', 0)
    # feature2 = Feature('Reliable', 'Our service is very reliable', 1)
    # feature3 = Feature('Easy to Use', 'Our service is easy to use', 2)
    # feature4 = Feature('Affordable', 'Our service is affordable', 3)
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def contact(request):
    return HttpResponse('<h1>Contact Page</h1>')

def counter(request):
    context = {
        'amount': len(request.POST['text'].split())
    }
    return render(request, 'counter.html', context)