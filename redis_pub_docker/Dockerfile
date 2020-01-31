FROM python:3
COPY redis_pub.py .
RUN pip install redis flask
ENV FLASK_APP redis_pub.py
CMD ["flask", "run", "--host=0.0.0.0"]