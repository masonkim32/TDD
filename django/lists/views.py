from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from lists.models import Item


class Homepage(TemplateView):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)

        list_url = reverse('todo_list')
        return redirect(to=list_url)


class TodoList(ListView):
    model = Item
