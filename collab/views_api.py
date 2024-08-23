from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from django.template.defaultfilters import slugify
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .perms import *


class BaseClubAPI:
    queryset = ClubModel.objects.all()
    serializer_class = ClubSerializer


class CreateClubAPIView(BaseClubAPI, CreateAPIView):
    # only for authenticated users.
    # POST: create new club.
    # Method "create" to set slug and author.
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        data['slug'] = slugify(data['name'])  # set field "slug" based in club name
        data['author'] = self.request.user.pk  # set field "author"
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListClubAPIView(BaseClubAPI, ListAPIView):
    # GET: list all clubs
    # admin only
    permission_classes = [IsAdminUser]


class ChangeClubAPIView(BaseClubAPI, RetrieveUpdateDestroyAPIView):
    # for admin or authors of a particular club
    # GET: detail a particular club
    # PUT, PATCH: edit club
    # DELETE: delete club
    lookup_field = 'slug'  # model field
    lookup_url_kwarg = 'slug'  # url value
    permission_classes = [IsAuthorOrAdmin]
