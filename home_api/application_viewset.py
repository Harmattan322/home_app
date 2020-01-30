from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import viewsets
from datetime import datetime

class AuthorizedViewset(viewsets.GenericViewSet):
    authentication_classes = [ TokenAuthentication ]
    permission_classes = [ IsAuthenticated ]

    @property
    def params(self):
        return self.request.query_params

    def parsed_date(self, str):
        try:
            return datetime.strptime(str, '%d.%m.%Y %H:%M')
        except:
            return None


class ReadOnlyViewset(viewsets.ReadOnlyModelViewSet, AuthorizedViewset):
    pass

class ApplicationViewset(viewsets.ModelViewSet, AuthorizedViewset):
    pass

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_superuser or request.method in permissions.SAFE_METHODS)

class AdminApplicationViewset(ApplicationViewset):
    permission_classes = [ IsAuthenticated, IsAdminOrReadOnly ]
