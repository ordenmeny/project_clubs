from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import views, viewsets
from .models import *
from .serializers import *
from copy import copy


# ReadOnlyModelViewSet - только для чтения
class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
