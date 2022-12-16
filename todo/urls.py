
from django.urls import path,include
from .views import (
    home,
    #fbv
    todo_list_created,
    todo_get_del_upd,

    #cbv
    Todos,
    TodosDetails,

    #mvs
    TodoMVS
    )

#For MVS IMPORT ROUTER 
from rest_framework import routers
router = routers.DefaultRouter()
router.register('todomvs', TodoMVS)

urlpatterns = [
    path('', home),

    #fbv urls
    path('todos/',todo_list_created),
    path('todos/<int:pk>/', todo_get_del_upd),
    
    #cbv
    path('todos_cbv/', Todos.as_view()),
    path('todos_cbv/<int:pk>', TodosDetails.as_view()), #classbaseviews 'de <int:pk> pk olarak yazilmali. Id olarak yazarsam hata verir

    #mvs
    path('', include(router.urls))

]


#####Put ile Patch farki Put'da güncellemek istedigim verinin bütün elemanlarini tekrardan göndermeliyim, güncellemeyecek olsam bile. Ama Patch'de cektigim verideki sadece güncellemek istedigim keywordü gönderebilirim.