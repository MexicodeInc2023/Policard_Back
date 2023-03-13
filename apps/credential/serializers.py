from pyexpat import model
from rest_framework.serializers import Serializer, ModelSerializer, CharField, ValidationError
from apps.credential.models import student, careers, request_reason, emergency_info
  
class careersSerializer(ModelSerializer):
    class Meta:
        model = careers
        fields = '__all__'
class careersUpdateSerializer(ModelSerializer):
    class Meta:
        model = careers
        fields = '__all__'

class studentSerializer(ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

class studentUpdateSerializer(ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

class request_reasonSerializer(ModelSerializer):
    class Meta:
        model = request_reason
        fields = '__all__'

class request_reasonUpdateSerializer(ModelSerializer):
    class Meta:
        model = request_reason
        fields = '__all__'

class emergency_infoSerializer(ModelSerializer):
    class Meta:
        model = emergency_info
        fields = '__all__'
class emergency_infoUpdateSerializer(ModelSerializer):
    class Meta:
        model = emergency_info
        fields = '__all__'
