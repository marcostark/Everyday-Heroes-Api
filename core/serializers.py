from rest_framework import serializers
from .models import CollectPoint


class CollectPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectPoint
        fields = '__all__'
