from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.serializers import ModelSerializer
from .models import *


class ClubSerializer(ModelSerializer):
    class Meta:
        # Fields slug and author will be set automatically in method "create"
        # in class CreateClubAPIView.
        # field "desc" - short description of the club (TextField).
        # field "text" - a full description of the club (CKEditor5Field).
        # field "required_team" - who is required in club (just a text).
        # field "request_team" - requests from users, who want to join in club.
        # field "valid_team" - users who have been approved.

        model = ClubModel
        fields = ['slug', 'name', 'author', 'desc',  # 'tags',
                  'text', 'required_team', 'request_team', 'valid_team']
