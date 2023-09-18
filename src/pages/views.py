from django.shortcuts import HttpResponse, render, Http404
from django.views.decorators.gzip import gzip_page

from menu.models import Pasta, Platter, RegularPizza, Salad, SicilianPizza, Sub

# Create your views here.

@gzip_page
def index(request):
    context = {
        "reg_pizza": RegularPizza.objects.all(),
        "sic_pizza": SicilianPizza.objects.all(),
        "subs": Sub.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "platters": Platter.objects.all()
    }
    return render(request, 'pages/index.html', context)
