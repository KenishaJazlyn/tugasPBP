from django.shortcuts import render
from django.http import HttpResponseRedirect,  HttpResponse
from main.forms import AddForm
from django.urls import reverse
from django.core import serializers

from main.models import Item


# Create your views here.
def show_main(request):
   items = Item.objects.all()

   context = {
      'name': 'Kenisha Jazlyn Malano', 
      'class': 'PBP E', 
      'items': items
   }

   return render(request, "main.html", context)


def add_product(request):
   form = AddForm(request.POST or None)

   if form.is_valid() and request.method == "POST":
      form.save()
      return HttpResponseRedirect(reverse('main:show_main'))

   context = {'form': form}
   return render(request, "add_product.html", context)

def show_xml(request):
   data = Item.objects.all()
   return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")