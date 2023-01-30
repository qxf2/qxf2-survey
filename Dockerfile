#Dockerfile
FROM python:3.8
WORKDIR /code/backend/app
ADD ./backend/requirements.txt /code/backend/requirements.txt
RUN apt update
RUN pip install -r /code/backend/requirements.txt
RUN apt install -y nodejs npm
EXPOSE 8000 3000
