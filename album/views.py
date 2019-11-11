from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images = Image.objects.all()
    locations =Location.get_locations() 
    return render(request,'album/index.html',{"images":images,"locations":locations})