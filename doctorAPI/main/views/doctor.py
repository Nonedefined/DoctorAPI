from rest_framework import generics
from main.models import Doctor
from main.serializers import DoctorSerializer
from main.filters import DoctorFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class PaginationDoctor(PageNumberPagination):   
    page_size = 2


class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.order_by('sort_number', 'name')
    serializer_class = DoctorSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = DoctorFilter
    pagination_class = PaginationDoctor


class DoctorDetail(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return self.queryset.filter(pk=self.kwargs['pk'])

