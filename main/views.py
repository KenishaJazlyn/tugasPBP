from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
       'appsName' : 'StockFlow',
       'name' : 'Kenisha Jazlyn Malano' ,
       'class' : 'PBP E'
    }
    return render(request, "main.html", context)