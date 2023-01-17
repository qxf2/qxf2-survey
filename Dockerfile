#Dockerfile
FROM python:3.8
WORKDIR /code/backend/app
COPY ./backend/requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY ./backend/app /code/backend/app
COPY ./frontend /code/frontend
EXPOSE 8000