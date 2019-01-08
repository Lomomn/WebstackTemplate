FROM python:3.6

WORKDIR /backend
COPY requirements.txt /backend
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

COPY . /backend
CMD uwsgi --ini uwsgi.ini --need-app