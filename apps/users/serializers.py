from django.forms import ValidationError
from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.hashers import make_password

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password']
    def validate(self, attrs):
        email = attrs.get('email', '')
        if email and User.objects.filter(email=email).exists():
            raise ValidationError({'email': 'El email ya existe'})
        name = attrs.get('name', '')
        if not name.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, write_only=True)
    email = serializers.EmailField()
    tokens = serializers.SerializerMethodField()
    
    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
    
    class Meta:
        model = User
        fields = ['id','name','password','statuscredential', 'email', 'tokens']
        read_only_fields = ['name','statuscredential']
        
    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        print(email)
        user = auth.authenticate(email=email,password=password)
        print(user)
        if not user:
            raise AuthenticationFailed('Credenciales no válidas, intenta de nuevo')
        if not user.is_active:
            raise AuthenticationFailed('La cuenta no está activa, contacta con soporte')
        return {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'statuscredential': user.statuscredential,
            'tokens': user.tokens
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
