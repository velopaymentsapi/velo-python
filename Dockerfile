FROM python:3.7.10-alpine

RUN apk update && apk add --no-cache --virtual .build-deps build-base
RUN apk add openssl-dev
RUN apk add gcc
RUN apk add musl-dev
RUN apk add git
RUN apk add python3-dev
RUN apk add build-base
RUN apk add libffi-dev
RUN apk add cargo
RUN apk add libc-dev
RUN apk del .build-deps gcc musl-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY test-requirements.txt ./
COPY tox.ini ./

RUN pip install cython
RUN pip install --no-cache-dir cryptography==2.1.4
RUN pip install --upgrade pip
RUN pip install tox
RUN pip install twine

CMD ["sh"]