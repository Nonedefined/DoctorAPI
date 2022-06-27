from rest_framework import serializers
from main.models import Direction


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ['id', 'name', 'slug', 'sort_number']


