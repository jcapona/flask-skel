FROM python:3.6-slim

WORKDIR /opt/server

COPY requirements.txt /opt/server/requirements.txt
RUN pip3.6 install -r requirements.txt

COPY . /opt/server

EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--chdir=/opt/server", "server:app"]
