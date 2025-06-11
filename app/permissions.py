from rest_framework import permissions


class GlobalDefaultPermissions(permissions.BasePermission):

    def __get_method(self, method):
        methods = {
            "GET": "view",
            "OPTIONS": "view",
            "HEAD": "view",
            "POST": "add",
            "PUT": "change",
            "PATCH": "change",
            "DELETE": "delete",
        }
        return methods.get(method, "")

    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_method(method)
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            return None

    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method, view=view
        )
        if not model_permission_codename:
            return False
        else:
            return request.user.has_perm(model_permission_codename)
