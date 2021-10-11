from django.shortcuts import render

# Create your views here.
def index(request):
    city = request.POST['city'] if request.method == 'POST' else ''
    return render(request, 'index.html', {'city': city})