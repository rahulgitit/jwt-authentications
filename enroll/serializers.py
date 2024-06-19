from rest_framework import serializers
from enroll.models import testdb


class testdbserializers(serializers.ModelSerializer):
    class Meta:
        model=testdb
        fields="__all__"