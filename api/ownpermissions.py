from rest_framework import permissions

# 本人以外ユーザーデータを編集・削除出来なくする
class ProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False