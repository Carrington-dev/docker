from python:3.12.1

LABEL label="0.0.1"
LABEL mantainer="Carrington Muleya <crn96m@gmail.com>"

RUN apt-get update
RUN apt-get upgrade -y

WORKDIR app/

ENV DJANGO_DB $DJANGO_DB
ENV DJANGO_USER $DJANGO_USER
ENV DB_NAME $DB_NAME
ENV DB_USER $DB_USER
ENV DB_HOST $DB_HOST
ENV DB_PASSWORD $DB_PASSWORD
ENV DB_PORT $DB_PORT

COPY . .

RUN pip3 install -r requirements.txt --no-cache

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]