from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def home(request):
    return render(request,'home-02.html')

# def login(request):
#     return render(request,'login.html')

# def register(request):
#     return render(request,'register.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def resetpassword(request):
    return render(request,'reset-password.html')

def shopingcart(request):
    return render(request,'shoping-cart.html')

def product(request):
    products =Product.objects.all()
    return render(request,'product.html',{'products':products})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def confirmation(request):
    return render(request,'confirmation.html')

def checkout(request):
    return render(request,'checkout.html')




from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method =="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register') 

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
            return redirect('register')

        user= User.objects.create_user(
        username=username,
        email=email,
        password=password
        )
        user.save()
        messages.success(request,"Account created successfully")
        return redirect('login')
    return render(request,'register.html')


from django.contrib.auth import authenticate,login

def user_login(request):
    if request.method=="POST" :
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password")
            return redirect('login')
    return render(request,'login.html')

from django.shortcuts import get_object_or_404

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})



from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Cart,Cartitem

def add_to_cart(request,product_id):
    product= get_object_or_404(Product,id=product_id)
    cart, created= Cart.objects.get_or_create(user=request.user)

    item, created = Cartitem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity +=1

    item.save()
    return redirect('cart')

def update_cart_item(request,item_id):
    item=get_object_or_404(
        Cartitem,
        id=item_id,
        cart__user=request.user
    )    

    if request.method =="POST":
        qty=int(request.POST.get('quantity',1))

        if qty>0:
            item.quantity=qty
            item.save()
        else:
            item.delete()

        return redirect('cart')
def cart_view(request):
    cart,created= Cart.objects.get_or_create(user=request.user)
    cart_items= Cartitem.objects.filter(cart=cart)

    return render(request, 'shoping-cart.html',{
        'cart':cart,
        'cart_items':cart_items
    })
def remove_item(request,id):
    item=get_object_or_404(Cartitem,id=id)
    item.delete()
    return redirect('cart')