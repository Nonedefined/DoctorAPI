from django.urls import path
from main.views import DirectionList, DoctorList, DoctorDetail


urlpatterns = [
    path('direction/', DirectionList.as_view()),
    path('doctor/', DoctorList.as_view()),
    path('doctor/<int:pk>/', DoctorDetail.as_view()),
]
