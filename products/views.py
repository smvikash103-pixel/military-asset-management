from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def cart(request):
    cart_data = request.session.get('cart', {})

    products = []
    total = 0

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(Product, id=product_id)

        subtotal = product.price * quantity
        total += subtotal

        products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'products/cart.html', {
        'products': products,
        'total': total,
    })