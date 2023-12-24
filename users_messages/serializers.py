from rest_framework import serializers
from users_messages.models import Message


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_read = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = ["id", "owner", "is_read", "receiver", "subject", "body", "created_at"]
