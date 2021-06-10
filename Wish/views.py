from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Wish.forms import WishCreateForm
from Wish.models import Wish, Product


@login_required
def create_wish(request):
    form = WishCreateForm(data=request.POST or None)

    if form.is_valid():
        wish = Wish(name=request.POST['name'], description=request.POST['description'], user=request.user)
        wish.save()
        if 'is_series' in request.POST:
            for i in range(int(request.POST['start_number']), int(request.POST['end_number']) + 1):
                Product(name=(wish.name + ' : ' + str(i)), number=i, wish=wish).save()
        else:
            Product(name=(wish.name + ' : 0'), number=0, wish=wish).save()

    context = {'formset': form}
    return render(request, "wish/create_wish.html", context)


@login_required
def get_wishes(request):
    wishes = []
    my_wishes = []

    for wish in Wish.objects.all():
        full_wish = FullWish(wish, Product.objects.filter(wish=wish).order_by('number'))
        if wish.user == request.user:
            my_wishes.append(full_wish)
            continue
        wishes.append(full_wish)

    context = {
        'wishes': wishes,
        'my_wishes': my_wishes,
    }
    return render(request, 'auth/show_wishes.html', context)


class FullWish:
    def __init__(self, wish, products):
        self.name = wish.name
        self.user = wish.user
        if len(products) == 0:
            self.products = []
        else:
            self.products = products

    def __str__(self):
        return self.user.username + " : " + self.name
