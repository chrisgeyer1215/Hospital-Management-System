from rest_framework import serializers
from .models import PatientAppointment,UserMessages



class PatientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientAppointment
        fields = '__all__'
        
        
class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserMessages
        fields = '__all__'