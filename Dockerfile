FROM python:3.6.5-alpine

RUN apk update && apk add git gcc python3-dev musl-dev build-base

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY test-requirements.txt ./
COPY tox.ini ./

RUN pip install tox

CMD ["sh"]