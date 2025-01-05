from datetime import datetime
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = RefreshToken(attrs['refresh'])
        data['exp'] = datetime.fromtimestamp(refresh.access_token['exp'])
        
        return data