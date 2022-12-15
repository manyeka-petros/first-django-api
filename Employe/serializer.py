from rest_framework import serializers
from .models import  Teachers

class TeeacherSerial(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['id','teach_name','password','email','salary','age','phone_numb']