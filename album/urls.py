from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.home,name="name"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(?P<location>\w+)',views.locate_image,name='location'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
