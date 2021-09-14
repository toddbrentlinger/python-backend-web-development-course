from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return HttpResponse('<h1>Contact Page</h1>')

def counter(request):
    context = {
        'amount': len(request.POST['text'].split())
    }
    return render(request, 'counter.html', context)