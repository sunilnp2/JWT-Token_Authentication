# from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers import UserRegisterSerializer, UserSignInSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from api.models import User


# function for get token and refresh token

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# class for registration 
class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer



# signin 
class UserSignInView(APIView):
    def post(self, request, format = None):
        serializer = UserSignInSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':["Username Or Password is not valid"]}},
                                status = status.HTTP_404_NOT_FOUND)
            


# -------------------------------------------PRACTICES------------------------------------------------------------

# class UserRegisterView(APIView):
#     def post(self, request, format = None):
#         serializer = UserRegisterSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save()
#             return Response({'msg':'Registered Successfully'},
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                


