from django.shortcuts import render
from .models import place
from .models import blog
from django.http import HttpResponse


# Create your views here.

def fun(request):
    obj = place.objects.all()
    blg = blog.objects.all()

    return render(request, 'index.html', {'results': obj,'outputs': blg})

    # blg = blog()
    # blg.name = "Bst tips to Trvl lght"
    # blg.decs = "Njot the journey"
