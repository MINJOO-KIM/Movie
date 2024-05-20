from rest_framework import serializers

from .models import Platform, Party

class PlatformListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Platform
        fields = '__all__'


class PartyCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Party
        fields = '__all__'
        read_only_fields = ('owner', 'participants')


class PartyListSerializer(serializers.ModelSerializer):
    partyId = serializers.IntegerField(source='id')
    platformId = serializers.IntegerField(source='platform.id')
    participants = serializers.IntegerField(source='participants.count', read_only=True)

    class Meta:
        model = Party
        fields = ('partyId', 'price', 'capacity', 'platformId', 'participants')