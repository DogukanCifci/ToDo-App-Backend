
from django.urls import path,include
from .views import (
    home,
    todo_list_created,
    todo_get_del_upd
    )

urlpatterns = [
    path('', home),
    path('todos/',todo_list_created),
    path('todos/<int:pk>/', todo_get_del_upd)
]