import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *


class ClubSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Club
        fields = ['pk', 'name', 'author', 'desc']
