from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import generics, permissions
from . import serializers
from . import models


class CollectPointListView(generics.ListCreateAPIView):

    queryset = models.CollectPoint.objects.all()
    serializer_class = serializers.CollectPointSerializer
    #filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    permission_classes = (permissions.IsAuthenticated,)
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = 'nome'
