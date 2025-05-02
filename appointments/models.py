from django.db import models
from datetime import date
from doctors.models import Doctors,TimeSlot



    
    


class PatientAppointment(models.Model):
    department_name=models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    appointment_date = models.DateField(default=date.today)
    timeslot=models.ForeignKey(TimeSlot,on_delete=models.CASCADE,related_name='appointments')
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_phone = models.CharField(max_length=15)
    reason_to_visit = models.TextField()
    
    
    def __str__(self):
        return f"Patient {self.patient_name} on {self.appointment_date} at {self.timeslot} with {self.doctor.doctor_name}"
    
    
    class Meta:
        unique_together = ('doctor', 'appointment_date', 'timeslot')


class UserMessages(models.Model):
    
    
    DEPARTMENT_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('General Medicine', 'General Medicine'),
        ('Dermatology', 'Dermatology'),
        ('Dentistry', 'Dentistry'),
        ('Ophthalmology', 'Ophthalmology')
        
    ]
    
    fullname=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    department=models.CharField(
        max_length=100,
        choices=DEPARTMENT_CHOICES,
        default='General Medicine',
    )
    message=models.CharField(max_length=1000)
    
    
    def __str__(self):
        return f"{self.fullname} has {self.message} for {self.department}"
    
    
    
    
