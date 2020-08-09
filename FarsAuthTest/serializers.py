from django.contrib.auth.models import User, Group
from rest_framework import serializers

#Serializer der bruges til at vise user, og fortaelle hvordan man opretter den
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		password = validated_data.pop('password')
		user = User(**validated_data)
		user.set_password(password)
		user.save()
		return user
