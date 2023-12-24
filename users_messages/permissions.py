from rest_framework import permissions

class MessagesPermissions(permissions.BasePermission):
    """
    Custom permission to: 
    Only owners allow to create object.
    Only owner or receiver can delete or read it.
    """

    def has_object_permission(self, request, view, obj):
        # Read/Delete permissions are allowed to owner/receiver request.
        if request.method in permissions.SAFE_METHODS or request.method == "DELETE":
            return obj.owner_id == request.user.id or obj.receiver_id == request.user.id


        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner_id == request.user
