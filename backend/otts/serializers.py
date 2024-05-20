from rest_framework import serializers

from .models import Platform

class PlatformListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Platform
        fields = '__all__'