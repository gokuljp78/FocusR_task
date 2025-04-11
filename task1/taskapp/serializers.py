from rest_framework import serializers
from .models import user



class UserSerializer(serializers.ModelSerializer):
    # id=serializers.UUIDField(read_only=True)
    # name=serializers.CharField()
    # ac_number=serializers.IntegerField()
    # mobile=serializers.IntegerField()
    class Meta:
        model = user
        fields = ( 'name', 'ac_number', 'mobile')