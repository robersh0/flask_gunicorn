FROM python:3.6

WORKDIR /flask_gunicorn

RUN pip install pip --upgrade


ADD ./backend/setup.py /flask_gunicorn/setup.py
RUN pip install -e .[dev]
RUN apt-get update && curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install nodejs && \
    npm i -g nodemon

EXPOSE 8000

ADD ./backend/model.pickle /flask_gunicorn/model.pickle
ADD ./backend/setup.cfg /flask_gunicorn/setup.cfg
ADD ./backend/wsgi.py /flask_gunicorn/wsgi.py
ADD ./backend/src /flask_gunicorn/src
