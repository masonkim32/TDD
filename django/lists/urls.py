from django.urls import path

from lists import views


app_name = 'lists'

urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('lists/new', views.NewList.as_view(), name='new_todo_list'),
    path('lists/<int:pk>/', views.TodoList.as_view(), name='todo_list'),
    path('lists/<int:pk>/add_item', views.AddItem.as_view(), name='add_item'),
]
