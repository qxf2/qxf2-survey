# Dockerfile
FROM python:3.8

# Set working directory
WORKDIR /code/backend/app

# Add and install requirements
ADD ./backend/requirements.txt /code/backend/requirements.txt
ADD ./frontend/package.json ./frontend/package-lock.json /code/react_node_packages/
ADD ./virtualized_employees_graphql_server/package.json /code/mock_server_node_packages/
RUN apt-get update && apt-get install -y curl gnupg
RUN pip install -r /code/backend/requirements.txt

# Add the Node.js package signing key
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -

# Install Node.js and npm
RUN apt-get install -y nodejs

#Install the node packages
RUN cd /code/react_node_packages && npm install
RUN cd /code/mock_server_node_packages && npm install

# Expose the required ports
EXPOSE 8000 3000 5000
