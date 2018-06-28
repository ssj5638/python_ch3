from django.shortcuts import render
from guestbook.models import Guestbook
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list':guestbook_list}
    return render(request, 'guestbook/index.html', context)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def deleteform(request):
    id_value = request.GET.get('id')
    context = {'id_value':id_value}
    return render(request, 'guestbook/deleteform.html',context)


def delete(request):
    id = request.POST.get('id')
    password = request.POST.get('password')
    Guestbook.objects.filter(id=id).filter(password=password).delete()

    return HttpResponseRedirect('/guestbook')
