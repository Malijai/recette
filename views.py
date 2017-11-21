# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from .models import Categorie,Contree,Ingredient,Quantite,Recette
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listingr(request):
    recette_list = Recette.objects.all()
    paginator = Paginator(recette_list, 15) # Show 15 post par page
    page = request.GET.get('page')
    try:
        recettes = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer, deliver first page.
        recettes = paginator.page(1)
    except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
        recettes = paginator.page(paginator.num_pages)
    return render(request, 'liste.html', {'recettes': recettes})


def view_recette(request, pk):
    recette = get_object_or_404(Recette, id=pk)
    ingredients = Quantite.objects.filter(recette_id=pk)

    return render_to_response('view_recette.html', {
                                'recette': recette,
                                'ingredients' : ingredients
                            })