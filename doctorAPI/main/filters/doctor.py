from django_filters import rest_framework
from django_filters.filters import OrderingFilter
from main.models import Doctor


class DoctorFilter(rest_framework.FilterSet):
    directions = rest_framework.Filter(field_name="directions__name", lookup_expr='icontains')
    experience = rest_framework.RangeFilter()

    order_by_field = 'sort_number'
    ordering = OrderingFilter(
        fields=(
            ('birthdate', 'birthdate'),
            ('experience', 'experience'),
        )
    )

    class Meta:
        model = Doctor
        fields = ['directions', 'experience']
