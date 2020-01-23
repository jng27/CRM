from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from reminder.models import toDoList


def reminders_list(request):
    template = loader.get_template('reminder.html')
    context = {}
    List = toDoList.objects.all()
    context["list"] = List
    print(context["list"])
    return HttpResponse(template.render(context,request))

def add_Reminders(request):
    ar = request.POST['content']
    new_object = toDoList(content=ar)
    new_object.save()
    template = loader.get_template('reminder.html') # {
    context = {}                                    #      FORCE RELOAD 
    List = toDoList.objects.all()                   #      ON BROWSER
    context["list"] = List                          #   }
    return HttpResponse(template.render(context,request))


def delete_Reminders(request, id):
    delete_item = toDoList.objects.get(id=id)
    delete_item.delete()
    template = loader.get_template('reminder.html') # {
    context = {}                                    #      FORCE RELOAD 
    List = toDoList.objects.all()                   #      ON BROWSER
    context["list"] = List                          #   }
    return HttpResponse(template.render(context,request))