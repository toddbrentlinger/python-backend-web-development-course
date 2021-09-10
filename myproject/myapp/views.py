from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Todd',
        'age': 33,
        'nationality': 'American',
    }
    return render(request, 'index.html', context)

def contact(request):
    return HttpResponse('<h1>Contact Page</h1>')