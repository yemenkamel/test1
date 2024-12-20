from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.request import HttpRequest, Request
from rest_framework import status

from .models import Parent, Student
from .serializers import ParentModelSerializer, ParentSerializer, StudentSerializer, StudentModelSerializer
from django.db.models import Q

from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def getAll(request:HttpRequest)->Response:
    parents= Parent.objects.all()
    ser= ParentModelSerializer(instance=parents, many= True)
    return Response(ser.data)

@api_view(['GET'])
def getById(request:HttpRequest, id:int)->Response:
    try:
        parent= Parent.objects.get(pk= id)
        ser= ParentModelSerializer(parent)
        return Response(ser.data)
    except Parent.DoesNotExist:
        return Response({
            "message": "does not exists"
        },status= status.HTTP_404_NOT_FOUND)
        
@api_view(['POST'])
def create(request:HttpRequest)->Response:
    ser= ParentModelSerializer(data= request.data)
    if ser.is_valid():
        ser.save()
        return Response(
            ser.data,
            status= status.HTTP_201_CREATED
        )
    return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, id):
    try:
        parent= Parent.objects.get(pk= id)
        ser= ParentModelSerializer(instance=parent, data= request.data)
        if ser.is_valid(raise_exception= True):
            ser.save()
            return Response(ser.data, status= status.HTTP_200_OK)
    except Parent.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete(request, id):
    try:
        parent = Parent.objects.get(pk= id)
        parent.delete()
        return Response()
    except Parent.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request:HttpRequest|Request, id:int= None)->Response:
    if request.method == "GET":
        if id:
            try:
                parent = Parent.objects.get(pk= id)
                ser= ParentSerializer(parent)
                return Response(ser.data)
            except Parent.DoesNotExist:
                return Response(status= status.HTTP_404_NOT_FOUND)
        parents= Parent.objects.all()
        ser= ParentSerializer(parents, many= True)
        return Response(ser.data)
    elif request.method == 'POST':
        ser= ParentSerializer(data= request.data)
        if ser.is_valid(raise_exception= True):
            ser.save()
            return Response(ser.data, status= status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        if id:
            try:
                parent= Parent.objects.get(pk= id)
                ser= ParentSerializer(instance=parent, data= request.data)
                if ser.is_valid(raise_exception= True):
                    ser.save()
                    return Response(ser.data, status= status.HTTP_200_OK)
            except Parent.DoesNotExist:
                return Response(status= status.HTTP_404_NOT_FOUND)
        return Response({
            "message": "please enter id"
        }, status= status.HTTP_400_BAD_REQUEST)
    else:
        if id:
            try:
                parent = Parent.objects.get(pk= id)
                parent.delete()
                return Response()
            except Parent.DoesNotExist:
                return Response(status= status.HTTP_404_NOT_FOUND)
        parents= Parent.objects.all()
        parents.delete()
        return Response()


@api_view(['GET'])
def getAllCategories(request:HttpRequest|Request):
    if request.version == '1.0':
        students= Student.objects.all()
        paginator= PageNumberPagination()
        paginator.page_size= 2
        pagenated_query = paginator.paginate_queryset(students, request)
        ser= StudentModelSerializer(pagenated_query, many= True)
        return paginator.get_paginated_response(ser.data)
    else:
        return Response({"v": Request.version})

@api_view(['POST'])
def createStudent(request:HttpRequest|Request)->Response:
    
    ser= StudentSerializer(data= request.data)
    if ser.is_valid(raise_exception= True):
        ser.save()
        return Response(ser.data, status= status.HTTP_201_CREATED)
    
@api_view(['GET'])
def sendMail(request):
    """ send_mail(
        'sour sub',
        'fcsdgc shafdjga jhasgd jhasgd',
        'maged.rajab@gmail.com',
        ['yemen2635@gmail.com'],
        fail_silently= False
    ) """
    html_content = render_to_string(
        "index.html",
        context={"name": 'yemen'},
    )
    msg = EmailMultiAlternatives(
        "Subject here",
        'hjgjj',
        'maged.rajab@gmail.com',
        ["yemen2635@gmail.com"],
        headers={"List-Unsubscribe": "<mailto:yemen2635@gmail.com>"},
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return Response()



