from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from gamestopapp.models import Cart, Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request,'index.html')


def create_product(request):

    if request.method == "GET":

        return render(request, 'createproduct.html', {'x': {}})
    
    else:

        name = request.POST['name']
        description = request.POST['description']
        manufacturer = request.POST['manufacturer']
        category = request.POST['category']
        price = request.POST['price']
        image = request.FILES['image']


        if not image:
            # Handle the case where the image is not provided
            return render(request, 'createproduct.html', {'error': 'Image is required.'})


        p = Product.objects.create(name = name, description = description, manufacturer = manufacturer, category = category, price = price, image = image)


        p.save()
        return redirect('/')
    


def read_product(request):

    p = Product.objects.all()

    context = {}

    context['data'] = p

    return render(request, 'readproduct.html', context)


def update_product(request, rid):
    
    if request.method == "GET":

        p = Product.objects.filter(id = rid)

        context = {}

        context['data'] = p

        return render(request, 'updateproduct.html', context)
    
    else:

        name = request.POST['name']
        description = request.POST['description']
        manufacturer = request.POST['manufacturer']
        category = request.POST['category']
        price = request.POST['price']

        p = Product.objects.filter(id = rid)

        p.update(name = name, description = description, manufacturer = manufacturer, category = category, price = price)

        return redirect("/read_product")
    


def delete_product(request, rid):
    product = get_object_or_404(Product, id=rid)
    product.delete()
    return redirect('/read_product')


def user_register(request):

    if request.method == "GET":

        return render(request, 'register.html')
    
    else:

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            u = User.objects.create(first_name = first_name, last_name = last_name, username = username, email= email)

            u.set_password(password)

            u.save()

            return redirect("/")
        else:

            return HttpResponse("Password and Confirm Password does not Match")




def user_login(request):

    if request.method == "GET":

        return render(request, 'login.html')
    
    else:

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:

            login(request, user)

            return redirect("/")
        
        else:

            context = {}
        

            context['error'] = "Password amd Username are Incorrect"

            return render(request, 'login.html', context)
        

def user_logout(request):

    logout(request)

    return redirect("/")



def create_cart(request, rid):

    prod = Product.objects.get(username = request.User)

    total_price = prod.price

    c = Cart.objects.create(product = prod, User = User, quantity = 1, total_price = total_price)

    c.save()

    return HttpResponse("Product Added to cart")

        
        




