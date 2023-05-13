<<<<<<< HEAD
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
=======
FROM docker.io/library/python:3.11.3-alpine3.16@sha256:0ba61d06b14e5438aa3428ee46c7ccdc8df5b63483bc91ae050411407eb5cbf4 AS builder

WORKDIR /EdgeGPT

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN apk add --no-cache make && \
make init && make build && make ci && apk del make && \
rm -Rf /root/.cache/pip


ENTRYPOINT ["python3", "-m" , "EdgeGPT"]
>>>>>>> fork_branch
