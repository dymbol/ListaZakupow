from django.contrib import admin
#import klasy z nazwy aplikacji
from manager.models import *

admin.site.register(BuyList)
admin.site.register(Element)
admin.site.register(ElementType)
admin.site.register(jednostka_miary)
admin.site.register(BuyListElement)

