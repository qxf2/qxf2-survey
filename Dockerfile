#Dockerfile
FROM python:3.8
WORKDIR /code/backend/app
ADD ./backend /code/backend
ADD ./frontend /code/frontend
ADD start.sh /code/backend/app
RUN apt update
RUN pip install -r /code/backend/requirements.txt
RUN apt install -y nodejs npm
RUN cd /code/frontend && npm install
EXPOSE 8000 3000