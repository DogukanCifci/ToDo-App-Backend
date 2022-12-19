from rest_framework import serializers

from .models import Todo

# class TodoSerializers(serializers.ModelSerializer):
#     todo_detail = serializers.HyperlinkedIdentityField(
#         view_name='todo-detail',
#     )

class TodoSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Todo #Burada hangi modeli kullanacagimni beliritiyorum.
        #fields = '__all__' # Burada da hangi field leri kullanacagimiz yaziyoruz. Hpesini göndereceksek __all__ yazabliriz. ama tek tek yazmak daha iyi.
        fields = (
            'id',
            'task',
            # 'todo_detail',  
            'description',
            'priority',
            'is_done',
            'created_date'
        )
