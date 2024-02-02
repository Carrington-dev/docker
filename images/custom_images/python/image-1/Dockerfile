# FROM python:alpine3.19
FROM ubuntu:latest

LABEL version="0.0.1"
LABEL mantainer="Carrington Muleya <from@stemgon.co.za>"


RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 -y

WORKDIR .

COPY . .

CMD ["python3", "./src/appy"]
