from django.conf.urls import url
from django.urls import  path
from . import views


urlpatterns = [
#    url(r'^$', listingr, name='listerecettes'),
    path('', views.listingr, name='listerecettes'),
    path('chercherecette/', views.get_cherchetexte, name='chercherecette'),
    path('<int:pk>/', views.view_recette, name='view_recette'),
]
