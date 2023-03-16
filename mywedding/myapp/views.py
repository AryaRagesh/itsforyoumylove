from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Year,Product

# Create your views here.

def index(request):
    return render(request, 'index.html')

def go(request):
    return render(request, 'users.html')

def ex(request):
    return render(request, 'contests.html')

def allyear(request,c_slug=None):
    c_page=None
    product_list=None

    if c_slug!=None:
        c_page=get_object_or_404(Year,slug=c_slug)
        product_list=Product.objects.all().filter(year_id=c_page)
    else:
        product_list=Product.objects.all()

    paginator=Paginator(product_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request,'images.html',{'category':c_page,'products':products})
