from django.db import models
import uuid

class Parent(models.Model):
    name= models.CharField(
        max_length= 250,
        unique= True,
        verbose_name= "Parent Name"
    )
    created_at= models.DateTimeField(
        auto_now_add = True
    )
    updated_at= models.DateTimeField(
        auto_now= True
    )
    
    class Meta:
        db_table= "parents"
        verbose_name= "Parent"
        verbose_name_plural= "Parents"
        
    def __str__(self) -> str:
        return self.name
        
class Student(models.Model):
    id= models.UUIDField(
        primary_key= True,
        editable= False,
        default= uuid.uuid4
    )
    first_name= models.CharField(
        max_length= 250
    )
    last_name= models.CharField(
        max_length= 250
    )
    parent= models.ForeignKey(
        Parent, 
        on_delete= models.DO_NOTHING,
        related_name= "students",
        related_query_name= "student"
    )
    birthday= models.DateField(null= True)
    note= models.TextField(default= "")
    image= models.ImageField(
        upload_to= 'images/students',
        max_length= 1000,
        null= True
    )
    
    class Meta:
        db_table= "students"
        unique_together= [
            ('first_name', 'last_name')
        ]
        verbose_name= "r"
        verbose_name_plural= "q"
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name + " " + self.parent.name