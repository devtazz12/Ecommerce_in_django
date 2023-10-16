from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required






# Create your views here.


def index(request):
    products=product.objects.all()[:15]
    if  request.user.is_anonymous:
        context={
            'products':products,
        }
    else:
        number_of_product_in_cart= cart.objects.filter(user=request.user)
        context={
            'products':products,
            'cart_products':number_of_product_in_cart,
            'total_amount':total_price(request)
        }
    return render(request, 'app/index.html', context)



def products(request):
    categories=category.objects.all()
    subcategories=subcategory.objects.all()
    products=product.objects.all()[:9]
    context={
        'products':products,
        'categories':categories,
        'subcategories':subcategories,
    }
    return render(request, 'app/products.html', context)

def signup(request):
    if request.method == "POST":
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')
        
        if User.objects.filter(username=username):
            messages.warning(request, "This user alredy exists please try the another user!!")
            return redirect('sign-in')
        
        if User.objects.filter(email=email):
            messages.warning(request, "email alredy exists please try the another email!!")
            return redirect('sign-in')
        
        if password == confirm_password :
            user= User.objects.create_user(
                username=username,
                password=password,
    
            )
            user.first_name=first_name
            user.email=email
            user.last_name=last_name
            user.is_active = False
            subject = 'welcome to D-com'
            message =render_to_string('app/email.html', {  
                'user': user,  
                'domain': get_current_site(request).domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
            user.save()
            messages.success(request,"Please confirm your email address to complete the registration")
            return redirect('signup')  
        else:
            messages.warning(request, "passord and confirm password doesn't match")
            return render(request, 'app/signin.html')

    return render(request, 'app/signin.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'account do not exists plz sign in')
    return render(request, 'app/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, f' you are logout !!')
    return redirect('signin')


def single_product(request, slug):
    prod=product.objects.get(slug=slug)
    related_prod=product.objects.filter(subcategory=prod.subcategory)
    context={
        'product':prod,
        'related_prod':related_prod
    }
    return render(request, 'app/product-single.html',context)

# product  cart
@login_required
def p_cart(request): 
    number_of_product_in_cart= cart.objects.filter(user=request.user)
    context={
        'products':number_of_product_in_cart
    }
    return render(request, 'app/cart.html', context)

@login_required
def add_to_cart(request, slug):
    prod=product.objects.get(slug=slug)
    if request.method=="POST":
        size=request.POST['size']
        quantity=request.POST['quantity']
        quantity_based_price= int(quantity) * prod.price
        try: 
           existing_prod=cart.objects.get(prod=prod)
        except cart.DoesNotExist:
            cart_info=cart.objects.create(
            user=request.user,
            prod=product.objects.get(slug=slug),
            size=size,
            quantity=quantity,
            quantity_based_price=quantity_based_price
        )
        cart_info.save()       
        return redirect('cart')
    else:
        try:
           prod=product.objects.get(slug=slug)    
           existing_prod=cart.objects.get(prod=prod)
        except cart.DoesNotExist:
            cart_info=cart.objects.create(
                user=request.user,
                prod=product.objects.get(slug=slug),
                quantity_based_price= prod.price
            )
            cart_info.save()

        return redirect('cart')


@login_required
def remove_from_cart(request, slug):
    prod=product.objects.get(slug=slug)
    cart_info=cart.objects.get(prod=prod)
    cart_info.delete()
    return redirect('cart')

def total_price(request):
    cart_product= cart.objects.filter(user=request.user)
    total_amount=0
    for i in cart_product:
        total_amount=total_amount + i.prod.price * i.quantity      
    return total_amount

@login_required
def checkout(request):
    cart_products=cart.objects.filter(user=request.user)
    context={
        'product':cart_products,
        "total_amount":total_price(request)
    }
    return render(request, "app/checkout.html", context)

def order(request):
    order=Order.objects.filter(user=request.user)
    context={
        'order':order
    }

    return render(request, 'app/order.html', context)

def place_order(request):
    cart_products=cart.objects.filter(user=request.user)
    place_order=Order.objects.create(
        user=request.user,
        total_amount=total_price(request) 
    )
    for i in cart_products:
        place_order.products.add(i.prod)
    place_order.save()
    cart_products.delete()
    return redirect('order')


def profile_details(request):
    user_profile=profile.objects.get(user=request.user)
    context = {
        'profile_info':user_profile
    }
    return render(request, 'app/profile-details.html', context)

def profile_details_update(request):
    if request.method == 'POST':
        profile_pic=request.FILES['image']
        email=request.POST['email']
        phone=request.POST['phone']
        date_of_birth=request.POST['date_of_birth']
        profile.objects.get(user=request.user).delete()
        user_detail=profile.objects.create(
            user=request.user,
            profile_img=profile_pic,
            date_of_birth=date_of_birth,
            phone_number=phone,
            email=email
        )
        user_detail.save()
        return redirect('profile_details')
    return render(request, "app/profile_details_update.html")

def dashboard(request):
    try:
        user_profile=profile.objects.get(user=request.user)
    except profile.DoesNotExist:
        user_detail=profile.objects.create(
            user=request.user,
            email=request.user.email
        )
        user_detail.save()
        return redirect('dashboard')

    context = {
        'profile_info':user_profile
    }
    return render(request, 'app/dashboard.html', context)



def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        messages.success(request,"Thank you for email confirmation now you can login !!")
        return redirect("signin") 
    else:
        messages.warning(request,"Activation link is invalid!")
        return redirect("signup")  


def error_404(request,  exception):
    return render(request, "app/404.html") 
        
    

