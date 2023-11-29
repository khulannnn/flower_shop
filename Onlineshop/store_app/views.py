from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product, Subcategory
import sqlite3
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    categories = Category.objects.all()
    subcategory = Subcategory.objects.all() 
    products = Product.objects.filter(is_available=True)
    context = {
        'categories': categories,
        'products': products,
        'subcategory': subcategory
    }
    return render(request, "index.html", context)
def cart(request):
    context = {}
    cart_product = request.session.get('cart')
    context = cart_product
    print(cart_product)

    if request.method == 'POST':
        context = {}
    return render(request, "cart.html",context=context)
def base(request):
    return render(request, "base.html")
def dashboard(request):
    return render(request, "dashboard.html")
def order_complete(request):
    return render(request, "order_complete.html")
def place_order(request):
    return render(request, "place-order.html")
def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    num = 0
    context = {
        'product': product,
    }
    if request.method == 'POST':
        name = request.POST.get('product_name')
        price = request.POST.get('product_price')
        color = request.POST.get('color')
        size = request.POST.get('size')	
        img = request.POST.get('product_image')
        num += 1
        context = {
            'product': product,
            'nof':num,
            'name':name,
            'price':price,
            'color':color,
            'size':size,
            'img':img
        }
        
        request.session['cart'] = {
            'name':name,
            'price':price,
            'color':color,
            'size':size,
            'product': product.id,
            'img':img
        }

            # addcart darahad ene ajilah ystoi 
        # new = Cart_item(userid = )
        # new.save()
        # count = Cart_item.objects.filter(userid=userid)
        # count = len(count)
        # context = {
        #     'count': count,
        # }

            # neg item  cart_item dotor hed bgaag medehiin tuld doodoh ajilna
        # co = Cart_item.objects.filter(productid=productid)

    return render(request, "product-detail.html", context)
def register(request):
    return render(request, "register.html")
def search_result(request):
    return render(request, "search-result.html")
def signin(request):
    return render(request, "signin.html")
def store(request, category_slug = None, subcategory_slug=None):
    
    con  = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("SELECT * FROM store_app_product")
    row = cur.fetchall()
    print(row)
    size = len(row)
    # Fetch all products that are available
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(is_available=True)

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        if subcategory_slug is not None:
            subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
            products = products.filter(subcategory=subcategory)

    all_products = Product.objects.all()
    paginator = Paginator(all_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, "store/store.html", context)
def home(request):
    categories = Category.objects.all()
    con  = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("SELECT * FROM store_app_product")
    row = cur.fetchall()
    print(row)
    size = len(row)
    # Fetch all products that are available
    products = Product.objects.filter(is_available=True)
    context = {
        'categories': categories,
        'products': products,
        'size': size,
    }
    return render(request, "home.html", context)