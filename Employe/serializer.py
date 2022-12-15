from rest_framework import serializers
from .models import  Teachers

class TeeacherSerial(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'