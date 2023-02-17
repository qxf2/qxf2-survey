# Dockerfile
FROM python:3.8

# Set working directory
WORKDIR /code/backend/app

# Add and install requirements
ADD ./backend/requirements.txt /code/backend/requirements.txt
ADD ./frontend/package.json ./frontend/package-lock.json /code/node_packages/
RUN apt update
RUN pip install -r /code/backend/requirements.txt
RUN apt install -y nodejs npm
RUN cd /code/node_packages && npm install

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

# Reset working directory
WORKDIR /code/backend/app

# Expose the required ports
EXPOSE 8000 3000 5000
