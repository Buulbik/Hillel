from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.order.forms import AddToCartForm, CreateOrderForm
from apps.order.models import Cart


def get_cart_data(user):
    cart = Cart.objects.filter(user=user)
    total = 0
    for row in cart:
        total += row.product.price * row.quantity
    return {'cart': cart, 'total': total}


@login_required
def add_to_cart(request):
    data = request.GET.copy()
    data.update(user=request.user)
    request.GET = data
    form = AddToCartForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        csrf = request.session.get('cart_token')
        if not csrf or csrf != data.get('csrfmiddlewaretoken'):
            row = Cart.objects.filter(product=cd['product'], user=cd['user']).first()
            if row:
                Cart.objects.filter(id=row.id).update(quantity=row.quantity + cd['quantity'])
            else:
                form.save()
            request.session['cart_token'] = data.get('csrfmiddlewaretoken')
        return render(request, 'order/added.html', {'product': cd['product'], 'cart': get_cart_data(cd['user'])})
    print(form.errors)


@login_required
def cart_view(request):
    cart = get_cart_data(request.user)
    return render(request, 'order/view.html', {'cart': cart})


@login_required
def creat_order(request):
    error = None
    user = request.user
    cart = get_cart_data(user)

    if not cart['cart']:
        return redirect('home')

    if request.method == 'POST':
        data = request.POST.copy()
        data.update(user=user, total=cart['total'])
        request.POST = data
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            form.save()
            Cart.objects.filter(user=user).delete()
            return render(request, 'order/created.html')
        error = form.errors
    else:
        form = CreateOrderForm(data={
            'first_name': user.first_name if user.first_name else '',
            'last_name': user.last_name if user.last_name else '',
            'email': user.email if user.email else '',
            'phone': user.phone if user.phone else '',
        })
    return render(request, 'order/create.html', {'cart': cart, 'form': form, 'error': error})
