FROM python:3
RUN pip install redis
WORKDIR /app
COPY app.py .
ENV APP_REDIS_HOST=redis
ENV APP_REDIS_PORT=6379
ENV APP_REDIS_CHANNEL=flask-channel
ENTRYPOINT [ "python", "app.py" ]