from django.urls import path
from . import views
from .views import PatientAppointmentCreateView,PatientAppointmentListView

urlpatterns = [
    path('list/', views.PatientAppointmentListView.as_view(), name='appointment-list'),
    path('create/', views.PatientAppointmentCreateView.as_view(), name='appointment-create'),
    path('message/',views.UserMessagesCreateView.as_view(),name="user_message")
]
