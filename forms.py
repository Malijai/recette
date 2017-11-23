# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


class RechercheForm(forms.Form):
    recherchetexte = forms.CharField(label='Texte à chercher', max_length=100)

