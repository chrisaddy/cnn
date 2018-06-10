FROM ubuntu:16.04
FROM python:3.6.3

ADD . /app
WORKDIR /app/

RUN pip install --user -r requirements.txt

CMD ["python", "app.py"]