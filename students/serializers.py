from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Parent,Student

class ParentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Parent
        fields= ['id', 'name', 'created_at']
        
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= '__all__'
        
class StudentSerializer2(serializers.Serializer):
    id= serializers.UUIDField(read_only= True)
    first_name= serializers.CharField(max_length=250)
    last_name= serializers.CharField(max_length=250)
    birthday= serializers.DateField()
    note= serializers.CharField(max_length= 250)
    
        
class ParentSerializer(serializers.Serializer):
    id= serializers.IntegerField(
        read_only= True
    )
    name= serializers.CharField(
        max_length= 10,
        min_length= 2,
        validators= [
            UniqueValidator(
                queryset= Parent.objects.all()
            )
        ],
    )
    students= StudentSerializer2(
        many= True
    )
    
    def create(self, validated_data:dict):
        students:list = validated_data.pop('students')
        parent= Parent.objects.create(**validated_data)
        for student in students:
            Student.objects.create(**student, parent= parent)
        return parent
    
    def update(self, instance:Parent, validated_data:dict):
        instance.name= validated_data.get("name", instance.name)
        instance.save()
        return instance
    
class StudentSerializer(serializers.Serializer):
    id= serializers.UUIDField(read_only= True)
    first_name= serializers.CharField(max_length=250)
    parent = serializers.PrimaryKeyRelatedField(
        queryset= Parent.objects.all()
    )
    parent_name= serializers.CharField(
        source= 'parent.name',
        read_only= True
    )
    parent_details= ParentSerializer(
        source= "parent",
        read_only=True
    )
    image= serializers.ImageField()
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)