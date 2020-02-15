from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, DetailView

from lists.models import Item, List


class Homepage(TemplateView):
    template_name = 'home.html'


class TodoList(ListView):
    model = Item

    def get_context_data(self, **kwargs):
        list_ = List.objects.get(id=self.kwargs['pk'])
        items = Item.objects.filter(list=list_)
        context_data = super().get_context_data(**kwargs)
        context_data.update({'items': items, 'list': list_})
        return context_data


class NewList(View):

    def post(self, request):
        new_list = List.objects.create()
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text, list=new_list)

        list_url = reverse('todo_list', kwargs={'pk': new_list.id})
        return redirect(to=list_url)


class AddItem(View):

    def post(self, request, **kwargs):
        list_ = List.objects.get(id=self.kwargs['pk'])
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text, list=list_)

        list_url = reverse('todo_list', kwargs={'pk': list_.id})
        return redirect(to=list_url)
