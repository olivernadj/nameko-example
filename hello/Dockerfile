FROM python:3.7-slim-stretch as base

RUN apt-get update && \
    apt-get install --yes curl netcat && \
    pip3 install --upgrade pip && \
    pip3 install virtualenv && \
    pip3 install nameko && \
    virtualenv -p python3 /appenv

ENV PATH=/appenv/bin:$PATH

RUN groupadd -r nameko && useradd -r -g nameko nameko && \
    mkdir /var/nameko/ && chown -R nameko:nameko /var/nameko/

COPY . /application

ENV PIP_WHEEL_DIR=/application/wheelhouse
ENV PIP_FIND_LINKS=/application/wheelhouse

WORKDIR /application

CMD ["nameko", "run", "--config", "config.yml", "helloworld"]