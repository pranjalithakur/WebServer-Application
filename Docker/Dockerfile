FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y php php-cgi python3 python3-pip
RUN python3 -m pip install python-magic pytz

WORKDIR /app
COPY ./Code/ /app/
EXPOSE 80
EXPOSE 443
CMD ["python3", "./server.py", "0.0.0.0", "443", "cert.pem", " key.pem"]