
from django.urls import path,include
from .views import (
    home,
    todo_list_created
    )

urlpatterns = [
    path('', home),
    path('students/',todo_list_created)
]