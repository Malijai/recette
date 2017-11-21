# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Categorie,Contree,Ingredient,Quantite,Recette

#class DocumentInline(admin.StackedInline):
class QuantiteInline(admin.TabularInline):
    model = Quantite

    fields = ['ingredient','quantite','unitee','dequoi']

class RecetteAdmin(admin.ModelAdmin):
#    admin.site.site_header = 'My admin'
    fieldsets = [
        ('Identification', {'fields': [('title', 'contree'), 'categorie','description']}),
        ('Instructions', {'fields': ['instructions',]}),
        ('Image', {'fields': ['photo']}),
        ('Temps', {'fields': ['preparation', 'cuisson']}),
    ]

    inlines = [QuantiteInline,]

    list_display = ('title', 'contree')

    list_filter = ['contree','categorie']


    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Recette, RecetteAdmin)
admin.site.register(Categorie)
admin.site.register(Ingredient)
admin.site.register(Contree)
admin.site.register(Quantite)

