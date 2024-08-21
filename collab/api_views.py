from django.forms import model_to_dict
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (RetrieveAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import views, mixins
from .models import *
from .serializers import *
from copy import copy
from rest_framework.permissions import IsAuthenticated
from .perms import *


class ClubAPIViewListCreate(ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = (IsAuthenticated,)


class ClubAPIViewDetail(RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = (IsAuthenticated,)


class ClubAPIViewChange(RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = (IsAuthenticated, IsAuthorPerm,)
    authentication_classes = (TokenAuthentication, )
