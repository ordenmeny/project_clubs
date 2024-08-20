import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class ClubModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class ClubSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


# Функция для преобразования объектов класса ClubModel в JSON-формат.
def encode():
    model = ClubModel('nm', 'hello')
    model_sr = ClubSerializer(model)  # model_sr.data - словарь

    # Преобразование объекта сериализации в json
    json = JSONRenderer().render(model_sr.data)
    print(json, sep='\n')


def decode():
    # Имитация поступления запроса от клиента в виде JSON:
    stream = io.BytesIO(b'{"title":"nm","content":"hello"}')

    # Формируем словарь из JSON
    data = JSONParser().parse(stream)
    print('data:', data)

    # Преобразовываем в объект сериализации
    serializer = ClubSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
