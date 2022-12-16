
from django.urls import path,include
from .views import (
    home,
    #fbv
    todo_list_created,
    todo_get_del_upd,

    #cbv
    Todos,
    TodosDetails
    )

urlpatterns = [
    path('', home),
    
    #fbv urls
    path('todos/',todo_list_created),
    path('todos/<int:pk>/', todo_get_del_upd),
    
    #cbv
    path('todos_cbv/', Todos.as_view()),
    path('todos_cbv/<int:pk>', TodosDetails.as_view()) #classbaseviews 'de <int:pk> pk olarak yazilmali. Id olarak yazarsam hata verir
]