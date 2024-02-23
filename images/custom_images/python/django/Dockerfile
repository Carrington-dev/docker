from python:3.12.1

LABEL label="0.0.1"
LABEL mantainer="Carrington Muleya <crn96m@gmail.com>"

RUN apt-get update
RUN apt-get upgrade -y

WORKDIR app/

COPY . .

RUN pip3 install -r requirements.txt

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]