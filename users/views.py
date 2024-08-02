from aiogram import Bot
from django.conf import settings
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import UserModel
from .forms import UserModelForm
from .serializers import *
from django.utils.crypto import get_random_string


# Регистрация пользователя.
# После введения данных происходит добавление уникального кода в поле telegram_verif_code.
class RegisterUserView(CreateView):
    template_name = 'registration/signup.html'
    model = UserModel
    form_class = UserModelForm

    # После создания пользователя перенаправляем
    def get_success_url(self):
        return reverse_lazy('users:login')

    # Логиним пользователя после регистрации
    def form_valid(self, form):
        form.instance.telegram_verif_code = get_random_string(length=16)
        valid = super().form_valid(form)
        login(self.request, self.object)

        return valid


# Ссылка на тг-бот из личного кабинета пользователя:
# https://t.me/startup_clubs_bot?start={{telegram_verif_code}}
# telegram_verif_code присваивается прт регистрации.
#
# Для общения с конкретным пользователем нужно получить chat_id.
# Пользователь нажимает на "/start". Происходит отправка chat_id
# сайту DRF посредством aiohttp. Происходит изменения поля chat_id
# текущего пользователя.
# Для связи учетной записи и сайта используется telegram_verif_code.


class UserDataAPIViewVerificationCode(RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # lookup_field указывает, по какому полю модели будет производиться поиск объекта.
    lookup_field = 'telegram_verif_code'
    # lookup_url_kwarg указывает на значение, по которому будет вестись поиск
    lookup_url_kwarg = 'verif_code'
