from rest_framework import serializers
from rest.models import User

# class UserSerializer(serializers.Serializer):
# 	username = serializers.CharField(max_length=30)

# 	def create(self,validated_data):
# 		return User.objects.create(**validated_data)

# 	def update(self,instance,validated_data):
# 		instance.username = validated_data.get('username',instance.username)
# 		instance.save()
# 		return instance

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username',)
			