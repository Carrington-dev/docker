FROM python:3.12.1

LABEL version="0.0.1"
LABEL maintainer="Carrington Muleya <crn96m@gmail.com>"

WORKDIR app/

COPY app/ .

RUN pip install -r requirements.txt


CMD ['python', 'app.py']