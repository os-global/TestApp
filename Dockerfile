FROM python:alpine

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000

# usage: create a docker image and run it
# docker build . -t test-app
# docker run --restart=always -d -p 8000:8000 test-app