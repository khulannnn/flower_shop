from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product, Subcategory, User
import sqlite3
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django.http import HttpResponse
# Create your views here.
def index(request):
    categories = Category.objects.all()
    subcategory = Subcategory.objects.all() 
    products = Product.objects.filter(is_available=True)
    user = request.session.get('id')
    context = {
        'categories': categories,
        'products': products,
        'subcategory': subcategory,
        'user':user
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
    context = {}
    cart_product = request.session.get('cart')
    context = cart_product
    return render(request, "place-order.html",context=context)
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
    if request.method == 'POST':
        try:

            phonenumber = request.POST.get("phonenumber")
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            password = request.POST.get("password")
            email = request.POST.get("email")

            if not all([phonenumber, firstname, lastname, password, email]):
                return render(request, "register.html", {'error_message': 'Please fill in all fields.'})

            con = sqlite3.connect('db.sqlite3')
            cur = con.cursor()

            # Check if the email already exists
            cur.execute(f"SELECT id FROM user WHERE email = ? AND phonenumber = ?", (email, phonenumber))
            existing_user = cur.fetchone()

            if existing_user:
                return render(request, "register.html", {'error_message': 'Email already in use. Please choose a different email.'})

            # Proceed with insertion
            cur.execute("""INSERT INTO user (firstname, lastname, phonenumber, email, password, usertypeid_id)
                        VALUES (?, ?, ?, ?, ?, 2)""", (firstname, lastname, phonenumber, email, password))
            con.commit()
        finally:
            con.close()
            return redirect('signin')
        
    return render(request, "register.html")
    
def search_result(request):
    return render(request, "search-result.html")

def signin(request):
    if request.method == 'POST':
        con = sqlite3.connect("db.sqlite3")
        cursor = con.cursor()
        phonenumber = request.POST.get("phonenumber")
        password = request.POST.get("password")
        

        # Ensure proper string formatting for SQL query
        query = f"SELECT id FROM user WHERE phonenumber = '{phonenumber}' AND password = '{password}'"
        cursor.execute(query)
        
        row = cursor.fetchone()

        if row:
            id = row[0]
            # Redirect upon successful login
            request.session['id'] = id
            return redirect('index')
        else:
            # Add an error message or handle incorrect login attempt
            error_message = "Invalid phone number or password. Please try again."
            return render(request, 'signin.html', {'error_message': error_message})
        
    # Render the signin.html template for GET requests
    return render(request, 'signin.html')



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
        try:
            cat = Category.objects.get(foo='bar')
        except Category.DoesNotExist:
            cat = Subcategory.objects.get(foo='bar')
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