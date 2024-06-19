from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from enroll.models import testdb
from enroll.serializers import testdbserializers
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# user=User.objects.all()
# for user in user:
#     token=Token.objects.get_or_create(user=user)
#     print(token)

class show_all_data(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=testdb.objects.all()
    serializer_class=testdbserializers
    
    