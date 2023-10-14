# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.10
WORKDIR /collector
COPY requirements.txt /collector
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /collector
EXPOSE 5000
