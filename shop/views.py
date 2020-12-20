from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def allProdCat(request, category_id=None):
    cat_page = None
    products_list = None
    if category_id != None:
        cat_page = get_object_or_404(Category, id=category_id)
        products_list = Product.objects.filter(category=cat_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)

    '''Pagination Code'''
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/category.html', {'category': cat_page, 'products': products})
        


def prodDetail(request, category_id, product_id):
    try:
        product = Product.objects.get(category_id=category_id, id=product_id)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product': product})
    
