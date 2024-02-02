from ubuntu:latest

LABEL version="0.0.1"
LABEL mantainer="Carrington Muleya <crn96m@gmail.com>"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 -y

WORKDIR /app

COPY app/ .

CMD ['python3', 'app.py']