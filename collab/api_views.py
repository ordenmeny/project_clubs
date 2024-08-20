from django.forms import model_to_dict
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import views
from .models import *
from .serializers import *
from copy import copy


class ClubAPICreateList(ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
