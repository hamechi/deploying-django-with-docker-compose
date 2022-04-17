from django.shortcuts import render

# Create your views here.

def petros(request):
    return render(request, 'coming_soon.html')
