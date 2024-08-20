from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from copy import copy


class ClubAPIView(APIView):
    def get(self, request):
        clubs = Club.objects.all()
        sr = ClubSerializer(instance=clubs, many=True)
        return Response({'clubs': sr.data})

    def post(self, request, *args, **kwargs):
        sr = ClubSerializer(data=request.data)
        sr.is_valid(raise_exception=True)
        sr.save()
        return Response({'club': sr.data})

    def put(self, request, *args, **kwargs):
        # Получить объект модели
        club = Club.objects.get(pk=kwargs['pk'])

        # Сериализация данных
        sr = ClubSerializer(instance=club, data=request.data)
        # Перед сохранением данных нужно выполнить валидацию.
        sr.is_valid(raise_exception=True)
        # Сохраняем данные
        sr.save()

        # Возвращаем измененные данные

        return Response({'club': sr.data})

    def delete(self, request, *args, **kwargs):
        club = Club.objects.get(pk=kwargs['pk'])
        sr = ClubSerializer(instance=club)
        sr.delete(club)

        return Response({'club': sr.data})
