from django.db.models import Q
from .models import Product
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def paginatorproducts(request,products,results):
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(products,results)

    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page=1
        products = paginator.page(page)
    except EmptyPage:
        page= paginator.num_pages
        products = paginator.page(page)
    
    left_index =(int(page)-1)
    if left_index < 1:
        left_index = 1
    
    right_index = (int(page)+2)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range =range(left_index,right_index)

    
    return custom_range,products



def searchproducts(request):
    search_query =''
    if request.GET.get('search'):
        search_query =request.GET.get('search')

    products=Product.objects.filter(
        Q(product_name__icontains=search_query)|
        Q(category__iexact=search_query)|
        Q(color__iexact=search_query)|
        Q(description__icontains=search_query)
    )

    return products,search_query

def searchcategory(request,categoryinput):
    search_query =''
    if request.GET.get('search'):
        search_query =request.GET.get('search')

    products=Product.objects.filter(
       Q(category=categoryinput),
        Q(product_name__icontains=search_query)or
        Q(category__iexact=search_query)or
        Q(color__iexact=search_query)or
        Q(description__icontains=search_query)
    )

    return products,search_query

