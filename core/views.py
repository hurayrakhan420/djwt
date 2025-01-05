from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from core.permissions import IsAuthenticatedWithJWT


User = get_user_model()

@api_view(['POST'])
def generate_jwt_token(request):
    email = request.data.get('email')
    client_secret = request.query_params.get('client_secret')
    
    print(email, client_secret)
    user = User.objects.filter(email=email).first()
    try:
        if user:
            refresh = RefreshToken.for_user(user)
            print(refresh.access_token['exp'])
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'exp': datetime.fromtimestamp(refresh.access_token['exp'])
            })
        else:
            user = User.objects.create_user(email=email)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'exp': refresh.access_token['exp']
            })
    except Exception as e:
        print(e)
        return Response({'error': f'Invalid credentials - {e}'}, status=400)


# hello world api
@api_view(['GET'])
@permission_classes([IsAuthenticatedWithJWT])
def hello_world(request):
    return Response({'message': 'hurayra khan!'})
