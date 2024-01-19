from ubuntu:latest

LABEL version="0.0.1"
LABEL mantainer="images@stemgon.co.za"

RUN apt-get update && apt-get upgrade -y

RUN apt-get nginx -y

EXPOSE 80

CMD ["nginx","-g","daemon off"]
