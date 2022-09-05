from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.order.forms import AddToCartForm
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
        row = Cart.objects.filter(product=cd['product'], user=cd['user']).first()
        if row:
            Cart.objects.filter(id=row.id).update(quantity=row.quantity + cd['quantity'])
        else:
            form.save()
        return render(request, 'order/added.html', {'product': cd['product'], 'cart': get_cart_data(cd['user'])})
    print(form.errors)


@login_required
def cart_view(request):
    cart = get_cart_data(request.user)
    return render(request, 'order/view.html', {'cart': cart})
