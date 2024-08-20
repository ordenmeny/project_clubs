from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class ClubAPIView(APIView):
    def get(self, request):
        lst_clubs = Club.objects.all().values()
        return Response({'clubs': list(lst_clubs)})  # Формирование ответа в виде json

    def post(self, request):
        post_new = Club.objects.create(
            name=request.data['name'],
            desc=request.data['desc'],
            author_id=request.data['author_id']
        )

        return Response({'post_data': model_to_dict(post_new)})
