from rest_framework import serializers
from api.models import User

# serializers for registration

class UserRegisterSerializer(serializers.ModelSerializer):
    # this field for password comfirmation
    password = serializers.CharField(style={'input_type': 'password'}, write_only = True)

    class Meta:
        model = User
        fields = ('username', 'profile', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

        # def validate(self, data):
        #     password = data.get('password')
        #     password2 = data.get('password2')
        #     if password != password2:
        #         raise serializers.ValidationError(
        #             "Password and Confirm password doesn't match.")

        # def UserRegisterSerializer.create(self, validate_data):
        #     return User.objects.create_user(
        #         **validate_data
        #     )


        

# serializers for userlogin

class UserSignInSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ('username', 'password')
