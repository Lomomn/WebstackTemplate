FROM python:3.6

WORKDIR /backend
COPY . /backend
RUN pip install -e .
RUN pip install '.[test]'
ENV FLASK_APP=entry
ENV FLASK_ENV=development

WORKDIR /backend
CMD uwsgi --ini uwsgi.ini --need-app