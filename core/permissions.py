from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication


class IsAuthenticatedWithJWT(BasePermission):
    def has_permission(self, request, view):
        jwt_authenticator = JWTAuthentication()
        try:
            jwt_authenticator.authenticate(request)
            return True
        except Exception as e:
            print(e)
            return False
