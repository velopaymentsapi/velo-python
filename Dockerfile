FROM python:3.6.5-alpine

RUN apk update && apk add --no-cache --virtual .build-deps openssl-dev gcc musl-dev git python3-dev build-base libffi-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY test-requirements.txt ./
COPY tox.ini ./

RUN pip install --upgrade pip
RUN pip install tox
RUN pip install twine

CMD ["sh"]