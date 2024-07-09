from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True},
            "date": {"read_only": True}
        }
