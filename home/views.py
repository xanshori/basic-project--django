from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from .models import Product
from .forms import ProductForm
from .utils import searchproducts,paginatorproducts,searchcategory
from django.contrib.admin.views.decorators import staff_member_required
import xlwt
import datetime
# Create your views here.

def index(request):
    products,search_query=searchproducts(request)
    categories = Product.objects.values('category').distinct()
    custom_range,products = paginatorproducts(request,products,6)

    
    context={
        'title':'HOME | PAGE',
        'categories':categories,
        'products':products,
        'search_query':search_query,
        'custom_range':custom_range,
    }
    return render(request,'home/index.html',context)

@staff_member_required(login_url='user:login')
def create(request):
    productforms=ProductForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if productforms.is_valid():
            productforms.save()
            return redirect('home:data')
    context={
        'title':'CREATE | PAGE',
        'productforms':productforms,
    }
    return render(request,'home/create.html',context)

@staff_member_required(login_url='user:login')
def data(request):
    products,search_query = searchproducts(request)
    context={
        'title':'DATA | PAGE',
        'products':products,
        'search_query': search_query
    }
    return render(request,'home/data.html',context)

@staff_member_required(login_url='user:login')
def datadelete(request,deleteinput):
    Product.objects.get(id=deleteinput).delete()
    return redirect('home:data')


@staff_member_required(login_url='user:login')
def dataupdate(request,updateinput):
    product= Product.objects.get(id=updateinput)
    productforms=ProductForm(request.POST or None, request.FILES or None,instance=product)
    if request.method =='POST':
        if productforms.is_valid():
            productforms.save()
            return redirect('home:data')
    context={
        'title':'UPDATE | PAGE',
        'productforms':productforms,
    }
    return render(request,'home/create.html',context)

def detail(request,detailinput):
    products = Product.objects.get(slug=detailinput)
    context={
        'title':'{}'.format(detailinput),
        'products':products,
    }
    return render(request,'home/detail.html',context)

def category(request,categoryinput):
    products,search_query=searchcategory(request,categoryinput)
    categories =Product.objects.values('category').distinct()
    custom_range,products = paginatorproducts(request,products,6)
    context={
        'title': 'CATEGORY | PAGE',
        'categories':categories,
        'products':products,
        'custom_range':custom_range,
        'search_query':search_query,
    }
    return render(request,'home/category.html',context)

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    
    response['Content-Disposition'] = 'attachment; filename="data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['product_code', 'product_name', 'color', 'create' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Product.objects.all().values_list('product_code', 'product_name', 'color', 'create')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num], datetime.datetime):
                date_time = row[col_num].strftime('%Y-%m-%d %H:%M:%S')
                ws.write(row_num, col_num, date_time, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response