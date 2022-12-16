from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
#my imports
from .models import Todo
from .serializers import TodoSerializer

def home(request) : 
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>')

@api_view(['GET', 'POST'])
def todo_list_created(request) :
    if request.method == 'GET' :
        todos = Todo.objects.all()
        #print("TODOS : ",todos)
        serializer = TodoSerializer(todos, many = True) # Birden fazla deger dönecegi icin many= True yazmam lazim. Yoksa hata ile karsilasirim.
        #print("SERIALIZER : ", serializer)
        #print("SERIALIZER DATA : " , serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        serializer = TodoSerializer(data=request.data)
        
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else :
            return Response(
                serializer.errors ,status = status.HTTP_400_BAD_REQUEST
            )
    
@api_view(['GET','PUT','DELETE'])
def todo_get_del_upd(request,pk) :

    todo = get_object_or_404(Todo, id=pk)

    if request.method == 'GET' :
        serializer = TodoSerializer(todo) # many=true koymam gerek yok cünkü tek bir object cekicem apiden
        return Response(serializer.data)

    elif request.method == 'PUT' :
        serializer = TodoSerializer(data = request.data , instance = todo) # instance=todo yazmak zorundayim put islemi yoaraken. Eslestirme yapmasi icin önemli. Yoksa o eslesen veriyi güncelleyecegine yeni veri ekler.

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else : 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' :
        todo.delete()
        return Response({
            'message' : 'Task Deleted Succesfully!'
        })