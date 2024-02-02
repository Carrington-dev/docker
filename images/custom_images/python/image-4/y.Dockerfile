FROM python:3.8-alpine

LABEL version="0.0.1"
LABEL maintainer="Carrington Muleya <crn96m@gmail.com>"

WORKDIR app/

COPY app/ .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["app.py" ]