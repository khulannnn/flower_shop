from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product
import sqlite3
# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, "index.html", context)
def cart(request):

    cart_product = request.session.get('cart')
    context = cart_product
    print(cart_product)
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
            'size':size
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
def store(request, category_slug = None):
    
    con  = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("SELECT * FROM store_app_product")
    row = cur.fetchall()
    print(row)
    size = len(row)
    # Fetch all products that are available
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category = categories)
        count=products.count()
    elif category_slug is None:
        products = Product.objects.filter(is_available = True)
        count=products.count()
    else:
        categories = Category.objects.all()
        products = Product.objects.filter(category = categories)
        count=products.count()
    context = {
        'products': products,
        'categories': categories,
        'count': count
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

