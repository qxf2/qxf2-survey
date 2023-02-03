# Dockerfile
FROM python:3.8

# Set working directory
WORKDIR /code/backend/app

# Add and install requirements
ADD ./backend/requirements.txt /code/backend/requirements.txt
RUN apt update
RUN pip install -r /code/backend/requirements.txt
RUN apt install -y nodejs npm

# Clone the qxf2-employees repository
RUN cd /code && git clone https://github.com/akkuldn/qxf2-employees.git

# Change the working directory
WORKDIR /code/qxf2-employees

# Install dependencies from the requirements file
RUN pip install -r requirements.txt

# Install SQLite3
RUN apt install sqlite3

# Create the SQLite database and import data
RUN  timeout 10 sqlite3 data/employee_database.sqlite3 -cmd '.mode csv' -cmd '.import data/dummy_data.csv employee'

# Update the secret file
RUN echo "JWT_SECRET_KEY='qxf2'" > employees/secret.py

# Add the allowed users file
RUN echo "USERS = {'dummy':'dummy', 'dummy1':'dummy1'}" > employees/allowed_users.py

# Reset working directory
WORKDIR /code/backend/app

# Expose the required ports
EXPOSE 8000 3000 5000
