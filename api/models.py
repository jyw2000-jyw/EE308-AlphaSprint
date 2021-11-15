from django.db import models
from datetime import datetime

class api(models.Model):
    #id = models.AutoField(primary_key=True) #主键可省略不写
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    addtime=models.DateTimeField(default=datetime.now)
    
    
    
    
    
    
    
    

    def __str__(self):
        return self.name+":"+self.phone

    class Meta:
       db_table="myapp_users"
