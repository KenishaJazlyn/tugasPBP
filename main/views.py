from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect,  HttpResponse
from main.forms import AddForm
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from main.models import Item
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
   items = Item.objects.filter(user=request.user)

   context = {
      'name': request.user.username,
      'class': 'PBP E', 
      'items': items,
      'last_login': request.COOKIES['last_login'],
   }

   return render(request, "main.html", context)

def register(request):
   form = UserCreationForm()
   if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
   context = {'form':form}
   return render(request, 'register.html', context) 

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
         login(request, user)
         response = HttpResponseRedirect(reverse("main:show_main")) 
         response.set_cookie('last_login', str(datetime.datetime.now()))
         return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_product(request):
   form = AddForm(request.POST or None)

   if form.is_valid() and request.method == "POST":
      item = form.save(commit=False)
      item.user = request.user
      item.save()
      return HttpResponseRedirect(reverse('main:show_main'))
   
   context = {'form': form}
   return render(request, "add_product.html", context)

def increment_quantity(request, product_id):
   item = Item.objects.get(id=product_id)
   item.amount += 1
   item.save()
   return redirect('main:show_main')

def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
   if request.method == 'POST':
      name = request.POST.get("name")
      amount = request.POST.get("amount")
      description = request.POST.get("description")
      user = request.user

      new_product = Item(name=name, amount=amount, description=description, user=user)
      new_product.save()

      return HttpResponse(b"CREATED", status=201)
   return HttpResponseNotFound()

@csrf_exempt
def delete_ajax(request, product_id):
   if request.method == 'DELETE':
      item = Item.objects.get(id=product_id)
      item.delete()

      return HttpResponse(b"DELETED", status=201)
   return HttpResponseNotFound()
@ensure_csrf_cookie
def increment_ajax(request, product_id):
   if request.method == 'POST':
      item = Item.objects.get(id=product_id)
      item.amount += 1
      item.save()
      return HttpResponse(b"INCREMENTED", status=201)
   return HttpResponseNotFound()
@ensure_csrf_cookie
def decrement_ajax(request, product_id):
   if request.method == 'POST':
      item = Item.objects.get(id=product_id)
      if item.amount > 0:
         item.amount -= 1
         item.save()
      return HttpResponse(b"DECREMENTED", status=201)
   return HttpResponseNotFound()


def get_product_json(request):
    product_item = Item.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', product_item))


def decrement_quantity(request, product_id):
   item = Item.objects.get(id=product_id)
   if item.amount > 0:
      item.amount -= 1
      item.save()
   return redirect('main:show_main')

def delete_item(request, product_id):
   product = Item.objects.get(id=product_id)
   product.delete()
   return redirect('main:show_main')


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


