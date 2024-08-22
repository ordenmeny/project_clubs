from rest_framework.serializers import ModelSerializer
from .models import *


class ClubSerializer(ModelSerializer):
    class Meta:
        model = ClubModel
        fields = ['slug', 'name', 'author', 'desc',  # 'tags',
                  'text', 'required_team', 'request_team', 'valid_team']

        read_only_fields = ['slug', 'author']
