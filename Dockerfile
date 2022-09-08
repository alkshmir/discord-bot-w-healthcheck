FROM python:3.10-slim-bullseye

RUN apt-get update \
    && apt-get -y install locales \
    && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

COPY src/ /root/src
COPY requirements.txt /root/src
WORKDIR /root/src

RUN pip install --upgrade pip && pip install --upgrade setuptools
RUN pip install -r requirements.txt

CMD ["python", "main.py"]