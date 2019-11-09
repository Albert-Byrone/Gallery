from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images = Image.objects.all()[::5]
    locations =Location.get_location() 
    return render(request,'album/index.html',{"images":images,"locations":locations})