from django.shortcuts import redirect, render
from django.urls import reverse

from lists.models import Item


def homepage(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)

        home_url = reverse('home')
        return redirect(to=home_url)

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
