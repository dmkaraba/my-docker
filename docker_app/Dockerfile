FROM python:3
RUN pip install redis flask
ENV APP_REDIS_HOST=redis
ENV APP_REDIS_PORT=6379
ENV APP_REDIS_CHANNEL=flask-channel
WORKDIR /app
ARG app
COPY $app ./app.py
ENTRYPOINT [ "python", "app.py" ]