from django.urls import path
from .views import DoctorsListCreateView, DoctorsDetailView, HospitalListView, ReviewCreateView
from doctors.views import DoctorsListView, TimeSlotListAPIView

urlpatterns = [
    path('create/',DoctorsListCreateView.as_view(),name='doctor-create'),
    path('list/', DoctorsListView.as_view(), name='doctor-list'),
    path('list/<str:department_name>',DoctorsListView.as_view(),name='doctor-department'),
    path('list/<str:department_name>/<str:doctor_name>/', DoctorsListView.as_view(), name='doctor-department-name'),
    path('list/<str:availabletoday>/',DoctorsListView.as_view(),name='doctor_availabletoday'),
    path('all/<str:qualified>/', DoctorsListView.as_view(), name='qualified'),
    path('timeslots/<int:doctor_id>/',TimeSlotListAPIView.as_view(),name='timeslot-lists'),
   

    path('detail/<str:doctor_name>/',DoctorsDetailView.as_view(),name='doctor-detail'), 
    path('hospitals/', HospitalListView.as_view(), name='hospital-list'),
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
]
