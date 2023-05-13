# This is a sample Dockerfile

# set base image python:3.8-slim-buster
FROM python:3.8-slim-buster

# set working directory as app
WORKDIR /app

# copy all items in current local directory (source) to current container directory (destination)
COPY . .

# Install the requirements specified in file using RUN
RUN pip3 install -r requirements.txt

# command to run when image is executed inside a container
CMD [ "python3", "./dcbot/bot.py" ]
