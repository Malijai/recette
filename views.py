# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, get_object_or_404
from .models import Quantite,Recette
from django.core.paginator import InvalidPage
from .forms import RechercheForm
from django.db.models import Q
from .paginationalpha import NamePaginator


def listingr(request):
    recette_list = Recette.objects.all()
    paginator = NamePaginator(recette_list, on="title", per_page=2)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        page = paginator.page(page)
    except InvalidPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'liste.html', {'page': page})


def view_recette(request, pk):
    recette = get_object_or_404(Recette, id=pk)
    ingredients = Quantite.objects.filter(recette_id=pk)

    return render_to_response('view_recette.html', {
                                'recette': recette,
                                'ingredients' : ingredients
                            })

def get_cherchetexte(request):
    form_class = RechercheForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            texte = request.POST.get('recherchetexte', '')
            recettes = Recette.objects.filter(Q(title__icontains=texte) | Q(instructions__icontains=texte))
            if recettes:
                return render(request, 'liste.html', {'recettes': recettes})
            else:
                return render(request, 'chercherecette.html', {'form': form_class, 'message': texte})
    else:
        form_class = RechercheForm()

    return render(request, 'chercherecette.html', {'form': form_class})