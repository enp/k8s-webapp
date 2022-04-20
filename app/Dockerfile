FROM python:latest
WORKDIR /app
RUN apt update -y && apt install -y iputils-ping bind9-dnsutils
RUN mkdir -p /app
COPY webapp.py /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 8080
USER 1:1
CMD python webapp.py
