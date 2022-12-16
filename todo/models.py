from django.db import models

class Todo(models.Model) : 
    PRIORITY = (
        (1,'High'),
        (2,'Medium'),
        (3,'Low'),
    )
    
    task = models.CharField(max_length=64)
    description =models.TextField()
    priority = models.IntegerField(choices=PRIORITY, default=3)
    is_done = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True) #Update edildiginde otomatik olarak o tarihi alir
    created_date = models.DateTimeField(auto_now_add=True) # Create edildiginde o tarihi ilk defasinda alir ve kaydeder.


    def __str__(self):
        return f'{self.task}'