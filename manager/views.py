#-*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
import json
from manager.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):

    return render_to_response('index.html')


def loginuser(request):
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return render(request, 'index.html', {'error_message': "Zalogowałeś się!", })
            else:
                # Return a 'disabled account' error message
                return render(request, 'login.html', {'error_message': "konto wyłączone", })
        else:
            return render(request, 'login.html', {'error_message': "błąd logowania", })
            # Return an 'invalid login' error message.
    else:
        return render(request, 'login.html', {})

def logoutuser(request):
    from django.contrib.auth import logout
    logout(request)
    return render(request, 'index.html', {})

@login_required(login_url='loginuser')
def elements_index(request):
    elements_list = Element.objects.all()
    context = {'elements_list': elements_list}
    return render_to_response('elements.html', context)

@login_required(login_url='loginuser')
def element_details(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    return render(request, 'element_details.html', {'element': element})

@login_required(login_url='loginuser')
def element_change_img(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    from help_functions import SearchWriteImage
    SearchWriteImage(element.name, element.id)
    return render(request, 'element_details.html', {'element': element})

@login_required(login_url='loginuser')
def element_del(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    nazwa = element.name
    element.delete()

    elements_list = Element.objects.all()
    context = {'elements_list': elements_list}
    return render_to_response('elements.html', context)

@login_required(login_url='loginuser')
def element_add(request, buylist_id=None):
    if request.method=="POST":
        #sprawdzanie czy słowniku post są takie klucze
        if request.POST.get('element') and request.POST.get('elementtype') and len(request.POST['element']) > 0 and len(request.POST['elementtype'])>0:
            name = request.POST['element']
            typ = request.POST['elementtype']
            # Redisplay the poll voting form.
            NewElement = Element(name=name, typeof_id=typ, picture='brak')
            NewElement.save()

            from help_functions import SearchWriteImage
            SearchWriteImage(NewElement.name, NewElement.id)
            if buylist_id is not None:
                '''Jesli użuytkownik chciał stworzyć element i od razu go dodać do listy zakupów'''
                NewBuyListElement = BuyListElement(element=NewElement, lista=get_object_or_404(BuyList, pk=buylist_id), quantity=1, jednostka=jednostka_miary.objects.get(name="sztuka/i"), active=True)
                NewBuyListElement.save()

                return buylist_details(request, buylist_id)
            else:
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return render(request, 'element_details.html', {'element': NewElement,'info_message': "Element został dodany"})
                #return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        else:
            typy_elementow = ElementType.objects.all()
            return render(request, 'element_add.html', {
                    'info_message': "Dokonaj wyboru!",
                    'typy_elementow': typy_elementow
                })
    #gdy form nie był wypełniony
    else:
        typy_elementow = ElementType.objects.all()
        context = {'typy_elementow': typy_elementow,"buylist_id":buylist_id}
        return render(request, 'element_add.html', context)

@login_required(login_url='loginuser')
def buylist_index(request):
    buylist_list = BuyList.objects.all()
    context = {'buylist_list': buylist_list}
    return render_to_response('buylist_index.html', context)


@login_required(login_url='loginuser')
def buylist_delete(request, buylist_id):
    list = get_object_or_404(BuyList, pk=buylist_id)
    this_list_elements = BuyListElement.objects.filter(lista=list)
    #usuwanie elementów listy
    id_listy=str(list.id)
    for x in this_list_elements:
        x.delete()
    #usunięcie listy
    list.delete()

    return render_to_response('buylist_index.html', {'info_message': "Lista nr "+id_listy+" usunięta"})


@login_required(login_url='loginuser')
def buylist_add(request):
    if request.method == "POST":
    #sprawdzanie czy słowniku post są takie klucze
        if request.POST.get('priority')  and len(request.POST['priority'])>0 :
            priority = request.POST['priority']
            import datetime
            p = BuyList(priority=priority,pub_date=datetime.datetime.now())
            p.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return render(request, 'buylist_index.html', {'info_message': "Lista nr " +str(p.id) + " dodana"})
        else:

            return render(request, 'buylist_add.html')
    #gdy form nie był wypełniony
    else:
        return render(request, 'buylist_add.html')


@login_required(login_url='loginuser')
def buylist_details(request, buylist_id=None):
    '''Funkcja wyswietla szczegóły listy zakupów.
    Parametry:
    buylist_idL id listy zakupów
    '''

    list = get_object_or_404(BuyList, pk=buylist_id)
    elements_list = []
    for x in BuyListElement.objects.filter(lista=list):
        elements_list.append(x)
    context={'list': list, 'elements_list': elements_list}

    #jeśli funkcjaa została wywołana po dodaniu nowego elementu

    return render(request, 'buylist_details.html', context)


@login_required(login_url='loginuser')
def get_element_list_by_type(request, elementtype_id):
    elements = Element.objects.filter(typeof=ElementType.objects.get(pk=elementtype_id))
    result = {}
    for element in elements:
        result[element.name]= element.id

    out=json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
    return HttpResponse(out, content_type='application/javascript')


@login_required(login_url='loginuser')
def buylist_add_elements(request, buylist_id):
    list = get_object_or_404(BuyList, pk=buylist_id)
    elements_list = Element.objects.all()
    elementtypes_list = ElementType.objects.all()
    jednostki = jednostka_miary.objects.all()

    if request.method == "POST":

        if len(request.POST['element_id']) >= 1:
            #został podanyy element do dodania
            x = BuyListElement(element=Element.objects.get(pk=int(request.POST['element_id'])), lista=list, quantity=request.POST['quantity'], jednostka=jednostka_miary.objects.get(name=request.POST['jednostka']), active=True)
            x.save()
            elements_list = []
            for x in BuyListElement.objects.filter(lista=list):
                elements_list.append(x)
            if request.POST['destination'] == "1":
                return render(request,  'buylist_details.html', {'list': list, 'elementtypes_list': elementtypes_list,'elements_list': elements_list, 'info_message': "Element dodany"})
            elif request.POST['destination'] == "2":
                context = {'elements_list': elements_list, 'list': list, 'jednostki': jednostki, 'elementtypes_list': elementtypes_list, 'info_message': 'Element dodany'}
                return render(request, 'buylist_add_elements.html', context)
        else:
            elements_list = []
            for x in BuyListElement.objects.filter(lista=list):
                elements_list.append(x)
                context = {'elements_list': elements_list, 'list': list, 'jednostki': jednostki, 'elementtypes_list': elementtypes_list}
                return render(request, 'buylist_add_elements.html', context)
    else:

        context = {'elements_list': elements_list, 'list': list, 'jednostki': jednostki, 'elementtypes_list': elementtypes_list}
        return render(request, 'buylist_add_elements.html', context)


@login_required(login_url='loginuser')
def buylist_add_element_status(request, buylistelement_id):
    element = BuyListElement.objects.get(pk=int(buylistelement_id))

    #zmiana statusu na "kupiony" lub "nie kupiony"
    if element.active is True:
        element.active = False
    else:
        element.active = True
    element.save()

    #powrót do listy zakupów z której pochodził ten element
    elements_list = []
    for x in BuyListElement.objects.filter(lista=element.lista):
        elements_list.append(x)
    return render(request, 'buylist_details.html', {'list': element.lista, 'elements_list': elements_list})

def buylist_element_status_ajax(request, buylistelement_id):
    element = BuyListElement.objects.get(pk=int(buylistelement_id))

    #zmiana statusu na "kupiony" lub "nie kupiony"
    if element.active is True:
        element.active = False
        active={"active":False}
    else:
        element.active = True
        active={"active":True}
    element.save()


    out=json.dumps(active, sort_keys=True, indent=4, separators=(',', ': '))
    return HttpResponse(out, mimetype='application/javascript')

@login_required(login_url='loginuser')
def buylist_element_delete(request, buylistelement_id):
    try:
        element = BuyListElement.objects.get(pk=int(buylistelement_id))
        element.delete()
        info_message = "Element znaleziony i usunięty"

        elements_list = []
        for x in BuyListElement.objects.filter(lista=element.list):
            elements_list.append(x)
        return render(request, 'buylist_details.html', {'list': list, 'elements_list': elements_list, 'info_message': info_message})
    except:
        info_message = "Brak takiego elementu"
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def buylist_element_get_comment(request, buylistelement_id):
    try:
        element = BuyListElement.objects.get(pk=int(buylistelement_id))
        comment={"comment":element.comment}
        out=json.dumps(comment, sort_keys=True, indent=4, separators=(',', ': '))
        return HttpResponse(out, mimetype='application/javascript')
    except:
        info_message = "Brak takiego elementu"
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def buylist_element_add_comment(request, buylistelement_id):
    if request.method == "POST":
        comment = request.POST['comment']
        element = get_object_or_404(BuyListElement, pk=int(buylistelement_id))
        element.comment = comment
        element.save()
        return HttpResponse("OK", mimetype='text/html')
        info_message = "Brak takiego elementu"
    else:
        return HttpResponse("Error: no POST data", mimetype='text/html')


