#Dockerfile
FROM python:3.8
WORKDIR /code/backend/app
COPY ./backend/requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY ./backend /code/backend
COPY ./frontend /code/frontend
COPY start.sh /code/backend/app
EXPOSE 8000