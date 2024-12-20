from django.db import models
from students.models import Student
import uuid

class Payments(models.Model):
    id= models.UUIDField(
        primary_key= True,
        editable= False,
        default= uuid.uuid4
    )
    student= models.ForeignKey(
        Student, on_delete= models.DO_NOTHING
    )
    date= models.DateTimeField(
        auto_now_add= True
    )
    payment= models.DecimalField(
        max_digits= 20,
        decimal_places= 4
    )
    payment_no= models.IntegerField(default= 1)
    notes = models.TextField(blank= True, default= "", db_column= "description")
    
    class Meta:
        db_table= "payments"
