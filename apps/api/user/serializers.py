from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        fields = '__al__'


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)

    class Meta:
        fields = '__al__'
