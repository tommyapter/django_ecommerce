from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ShippingAddressForm
from .models import (Customer,
                    Product,
                    Order,
                    OrderItem,
                    ShippingAddress,
                    )


def store(request):
    products = Product.objects.all()
    context = {'products':products}

    try:
        customer = request.user.customer
        # order = Order.objects.get(customer=customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total_items = order.get_cart_items
    except:
        total_items = 0
    context['total_items']=total_items

    return render(request, 'store/store.html', context)


@login_required(login_url="/accounts/signup")
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all().order_by('date_added')

    total_items = order.get_cart_items
    context = {'items':items, 'order':order,
            'total_items':total_items}

    return render(request, 'store/cart.html', context)


@login_required(login_url="/accounts/signup")
def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    total_items = order.get_cart_items

    try:
        obj = ShippingAddress.objects.get(order = order)
        form = ShippingAddressForm(request.POST or None, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('../payment/')
    except:
        form = ShippingAddressForm(request.POST or None, instance = None)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.customer = customer
            shipping.order = order
            shipping.save()
            return redirect('../payment/')

    context = {'items':items, 'order':order,
                'total_items':total_items, 'form':form}

    return render(request, 'store/checkout.html', context)

@login_required(login_url="/accounts/signup")
def payment(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    total_items = order.get_cart_items
    # shipping = ShippingAddress.objects.get(order = order)
    shipping = get_object_or_404(ShippingAddress, order = order)

    context = {'items':items, 'order':order,
                'total_items':total_items, 'shipping':shipping}
    return render(request, 'store/payment.html', context)





@login_required(login_url="/accounts/signup")
def add_to_cart(request, product_id):
    # if request.method == 'POST':
    product = get_object_or_404(Product, pk=product_id)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)
    orderitem.quantity += 1
    orderitem.save()
    # messages.success(request, "Cart updated!")
    return redirect('../')


@login_required(login_url="/accounts/signup")
def add_one(request, orderitem_id):
    orderitem = get_object_or_404(OrderItem, pk=orderitem_id)
    OrderItem.objects.get(pk=orderitem_id)
    orderitem.quantity += 1
    orderitem.save()
    return redirect('../cart/')

@login_required(login_url="/accounts/signup")
def remove_one(request, orderitem_id):
    orderitem = get_object_or_404(OrderItem, pk=orderitem_id)
    OrderItem.objects.get(pk=orderitem_id)
    orderitem.quantity -= 1
    orderitem.save()
    if orderitem.quantity == 0:
        orderitem.delete()

    return redirect('../cart/')


@login_required(login_url="/accounts/signup")
def process_order(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    print('order')
    order.complete = True
    order.save()
    return redirect('../')
