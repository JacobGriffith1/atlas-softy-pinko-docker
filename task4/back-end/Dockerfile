# To create a Docker image, you will need to
# utilize a Dockerfile.
# Create a Dockerfile that:

# Is based on the latest ubuntu
FROM ubuntu:22.04

# Update APT using apt-get update
RUN apt-get update

# Upgrade currently installed software through
# APT using apt-get upgrade -y
RUN apt-get upgrade -y

# Install python3, python3-pip, and flask
    # Note: Make sure to automatically install and skip user
    # input with the “-y” flag for apt-get
    # Note: flask must be installed with pip3,
    # not through apt-get
RUN apt-get install -y python3 python3-pip
RUN pip3 install flask

# In your Dockerfile, use /app as the working directory and
# copy the Python file to your Docker image
WORKDIR /app
COPY api.py /app/api.py

# When running your Docker image, your Flask server should
# spin up and accept requests
    # You will need to make sure that you forward the Docker
    # container’s port 5252 to the host machine’s port 5252
    # when running your image in a container.
EXPOSE 5252
