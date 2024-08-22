from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .perms import *


class BaseClubAPI:
    queryset = ClubModel.objects.all()
    serializer_class = ClubSerializer


class CreateClubAPIView(BaseClubAPI, CreateAPIView):
    # only for authenticated users
    permission_classes = [IsAuthenticated]


class ListClubAPIView(BaseClubAPI, ListAPIView):
    # admin only
    permission_classes = [IsAdminUser]


class ChangeClubAPIView(BaseClubAPI, RetrieveUpdateDestroyAPIView):
    # for admin or authors of a particular club
    lookup_field = 'slug'  # model field
    lookup_url_kwarg = 'slug'  # url value
    permission_classes = [IsAuthorOrAdmin]
