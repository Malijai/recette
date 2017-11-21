from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)

    class Meta:
       ordering = ['nom']

    def __str__(self):
        return '%s' % self.nom

    def __unicode__(self):
        return u'%s' % self.nom


class Contree(models.Model):
    nom = models.CharField(max_length=200)

    class Meta:
       ordering = ['nom']

    def __str__(self):
        return '%s' % self.nom

    def __unicode__(self):
        return u'%s' % self.nom


class Ingredient(models.Model):
    nom = models.CharField(max_length=200, unique=True)
    sorte = models.CharField(max_length=200, default='-')
    description = models.CharField(max_length=200, default='-')

    class Meta:
       ordering = ['nom']

    def __str__(self):
        return '%s' % self.nom

    def __unicode__(self):
        return u'%s' % self.nom


class Recette(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    contree = models.ForeignKey(Contree)
    description = models.CharField(max_length=250)
    cuisson = models.IntegerField()
    preparation = models.IntegerField()
    image = models.CharField(max_length=200,blank=True, null=True,)
    categorie = models.ManyToManyField(Categorie)
#    quantite = models.ManyToManyField(Quantite)
    photo = models.ImageField(upload_to="images", verbose_name="Illustration", blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return '%s' % self.title

    def __unicode__(self):
        return u'%s' % self.title


class Quantite(models.Model):
    recette = models.ForeignKey(Recette)
    ingredient = models.ForeignKey(Ingredient)
    quantite = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    unitee = models.CharField(max_length=30, blank=True, null=True)
    dequoi = models.CharField(max_length=200, default='-')

    class Meta:
       ordering = ['dequoi','ingredient']

    def __str__(self):
        return '%s %s %s %s' % (self.dequoi, self.ingredient, self.quantite, self.unitee)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.dequoi, self.ingredient, self.quantite, self.unitee)