from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView

from lists.models import Item


class Homepage(TemplateView):
    template_name = 'home.html'


class TodoList(ListView):
    model = Item


class NewList(View):

    def post(self, request):
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)

        list_url = reverse('todo_list')
        return redirect(to=list_url)
