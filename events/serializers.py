from .models import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    organizer  = serializers.HiddenField(default=serializers.CurrentUserDefault())
    participants  = serializers.HiddenField(default=[])

    class Meta:
        model = Event
        fields = '__all__'
