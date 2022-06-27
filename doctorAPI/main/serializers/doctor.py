from rest_framework import serializers
from main.models import Doctor, Direction


class DoctorDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ('name', 'slug', 'sort_number', )


class DoctorSerializer(serializers.ModelSerializer):
    directions = DoctorDirectionSerializer(many=True, )

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'slug', 'directions', 'description', 'birthdate', 'experience', 'sort_number']
