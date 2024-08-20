import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *


class ClubSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    desc = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Club.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.save()

        return instance

    def delete(self, instance):
        instance.delete()
        return 'Club was deleted'
