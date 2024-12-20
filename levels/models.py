from django.db import models
import uuid
from students.models import Student

class Level(models.Model):
    id= models.UUIDField(
        primary_key= True,
        editable= False,
        default= uuid.uuid4
    )
    name= models.CharField(
        max_length= 250,
        unique= True
    )
    
    class Meta:
        db_table= "levels"
        
class LevelStudent(models.Model):
    id = models.UUIDField(
        primary_key= True,
        editable= False,
        default= uuid.uuid4
    )
    level= models.ForeignKey(
        Level,
        on_delete= models.DO_NOTHING
    )
    student= models.ForeignKey(
        Student,
        on_delete= models.DO_NOTHING
    )
    
    class Meta:
        db_table= "leves_students"