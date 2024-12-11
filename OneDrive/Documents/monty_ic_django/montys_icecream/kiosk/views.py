from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem

def add_to_cart(request, product_id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if request.method == 'POST':
        form = AddToCartForm(request.POST, instance=cart_item)
        if form.is_valid():
            cart_item.quantity += form.cleaned_data['quantity']
            cart_item.save()
            return redirect('view_cart')

    else:
        form = AddToCartForm()

    return render(request, 'add_to_cart.html', {'form': form, 'product': product})

def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'view_cart.html', {'cart': cart})

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.cart.user == request.user:
        item.delete()
    return redirect('view_cart')


def menu(request):
    return render(request, 'kiosk/menu.html')

def cones(request):
    return render(request, 'kiosk/cones.html') 

def cakes(request):
    return render(request, 'kiosk/cakes.html')

def milkshakes(request):
    return render(request, 'kiosk/milkshakes.html')

def froyo(request):
    return render(request, 'kiosk/froyo.html')

def sandwiches(request):
    return render(request, 'kiosk/sandwiches.html')   

def home(request):
    return render(request, 'kiosk/home_page.html')

