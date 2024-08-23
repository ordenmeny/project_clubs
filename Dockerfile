FROM python:3.11-alpine3.19

ENV PYTHONUNBUFFERED=1

RUN mkdir /django_app
WORKDIR /django_app
COPY req.txt .

RUN pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps build-base postgresql-dev musl-dev && \
    pip install -r req.txt && \
    apk del .tmp-deps && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
#     chown -R app:app /vol && \
#     chmod -R 755 /vol


COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
