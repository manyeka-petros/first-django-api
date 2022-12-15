from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Teachers
from .serializer import TeeacherSerial

# Create your views here.

class Employ(APIView):
    def _get(request):
        teachers = Teachers.objects.all()
        serialize = TeeacherSerial(teachers,many = True)
        return Response(serialize.data)
    
