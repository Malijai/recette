from django.conf.urls import url
from . import views
from .views import listingr, view_recette

urlpatterns = [
#    url(r'^$', BlogIndex.as_view(), name='blogindex'),
#    url(r'^$', listingr, name='listerecettes'),
    url(r'liste.html', listingr, name='listerecettes'),
    url(r'^(?P<pk>[-\w]+)/$', view_recette, name='view_recette'),
]
