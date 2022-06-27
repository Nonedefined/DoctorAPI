from rest_framework import generics
from main.models import Direction
from main.serializers import DirectionSerializer


class DirectionList(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

