from rest_framework import viewsets, mixins

from rest_framework.response import Response
from rest_framework.exceptions import bad_request

from users_messages.models import Message
from users_messages.serializers import MessageSerializer
from users_messages.permissions import MessagesPermissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class MessagesViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Provide 'list', 'retrieve', 'create', 'delete', for the owner of the message.
    Provide 'list', 'retrieve' and 'delete', for the receiver.
    """

    queryset = Message.objects.select_related("owner", "receiver")
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, MessagesPermissions]

    def get_queryset(self):
        """Allow current user to access to his outbox (messages that he is the owner)"""
        if self.action == "list":
            self.queryset = Message.objects.filter(
                owner=self.request.user
            ).select_related("owner", "receiver")

        return super().get_queryset()

    def perform_create(self, serializer):
        """associate current user with the message"""
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        retrieve single message.
        if the user is the receiver - flag the message.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        res = Response(serializer.data)
        if self.request.user and self.request.user.id == instance.receiver_id:
            instance.is_read = True
            instance.save()
        return res

    @action(detail=False)
    def inbox(self, request, *args, **kwargs):
        """Allow current user to access to his inbox (messages that he is the receiver)"""
        is_read = self.request.query_params.get("is_read")
        messages = self.queryset.filter(receiver=self.request.user)
        if is_read:
            if is_read in ("True", "False", "0", "1"):
                messages = messages.filter(is_read=is_read)
            else:
                return bad_request(
                    request=self.request, exception="Invalid query parameter"
                )

        page = self.paginate_queryset(messages)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(messages, many=True)
        return Response(serializer.data)
