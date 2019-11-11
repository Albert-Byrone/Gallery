from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images = Image.objects.all()
    locations =Location.get_locations() 
    return render(request,'album/index.html',{"images":images,"locations":locations})

def locate_image(request,location):
    images = Image.filter_by_location(location)
    return render(request,'album/location.html',{"located_images":images})

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get("search")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        
        return render(request, 'album/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'album/search.html', {"message": message})
