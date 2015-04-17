#-*- coding: utf-8 -*-
from django.db import models


class BuyList(models.Model):
    #obiekt listy zakupów
    priority = models.IntegerField()
    pub_date = models.DateTimeField('Data utworzenia')
    active =models.BooleanField(default=1)


#Typy elementów. np.: warzywa, nabiał	
class ElementType(models.Model):
    name =  models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        #sortowanie elementów po nazwie
        ordering = ['name']


#bazowe elementy z których budujemy listę zakupów, np.: jabłko
class Element(models.Model):
    name =  models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    typeof = models.ForeignKey(ElementType)
    ordering = ['name']

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        #sortowanie elementów po nazwie
        ordering = ['name']


#Jednostka np.: kg, sztuk etc
class jednostka_miary(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    class Meta:
        #sortowanie elementów po nazwie
        ordering = ['name']


#elemnty składowe konkretnej listy zakupów
class BuyListElement(models.Model):
    element = models.ForeignKey(Element)
    lista = models.ForeignKey(BuyList)
    quantity = models.IntegerField(default=0)
    jednostka = models.ForeignKey(jednostka_miary)
    active = models.BooleanField(default=1)
    comment = models.TextField()


