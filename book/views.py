from django.shortcuts import render
from .models import *
from .serializers import * 
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response



# viewSets

class Studentviewset(viewsets.ViewSet):
    def list(self,request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset,many = True)
        return Response(serializer.data)     

    def retrieve(self,request,pk=None ):
        id = pk
        if id is not None: 
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset,many = True)
            return Response(serializer.data)
        
    def update(self,request,pk):
        id = pk
        queryset = Student.objects.get(id=id)
        serializer = StudentSerializer(queryset,many = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"completed data updated"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        id = pk
        queryset= Student.objects.get(pk=id)
        queryset.delete()
        return Response({'msg': "message deleted"})

    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"completed data created "})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#Concrete generic Api Views

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  

class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# combinational Api Views
class Studentlc(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Studentrup(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRD(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

