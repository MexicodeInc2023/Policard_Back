from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserView(APIView):
    def get(self, request, format=None):
        token = request.COOKIES.get('jwt')
        # Verificamos si el token existe
        if not token:
            raise AuthenticationFailed('No se ha autenticado')
        # Verificamos si el token es válido
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        # Si el token expiró, se lanza una excepción
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Sesión expirada')
        # Obtenemos el usuario
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)      
        return Response(serializer.data)   
