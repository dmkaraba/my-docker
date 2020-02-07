FROM python:3
RUN pip install redis flask
ENV APP_REDIS_HOST=redis
ENV APP_REDIS_PORT=6379
ENV APP_REDIS_CHANNEL=flask-channel
WORKDIR /app
ARG app
ARG healthcheck
COPY $app ./app.py
COPY $healthcheck ./healthcheck.sh
HEALTHCHECK CMD ./healthcheck.sh
ENTRYPOINT [ "python", "app.py" ]