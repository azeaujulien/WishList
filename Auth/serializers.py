from rest_framework import serializers

from .models import Account, RegisterKey
from Wish.serializers import BasicWishSerializer
from Wish.models import Wish


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, **kwargs):
        user = Account(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        return user


class BasicAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email']


class AccountSerializer(serializers.ModelSerializer):
    wishes_create = serializers.SerializerMethodField('get_wishes_create')
    wishes_taken = serializers.SerializerMethodField('get_wishes_taken')

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'wishes_create', 'wishes_taken']

    def get_wishes_create(self, account):
        return BasicWishSerializer(Wish.objects.filter(user=account).order_by('-created_at'), many=True).data

    def get_wishes_taken(self, account):
        return BasicWishSerializer(Wish.objects.filter(taker=account).order_by('-taken_at'), many=True).data


class DetailedAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'is_active', 'is_staff', 'is_admin', 'is_superuser', 'date_joined', 'last_login']


class RegisterKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterKey
        fields = ['id', 'key', 'created_at']
