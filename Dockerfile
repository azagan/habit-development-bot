FROM python:3.9.2-alpine

ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /src
WORKDIR /src
COPY . /src

COPY requirements.txt /tmp/
RUN apk update \
    && apk add --no-cache --virtual .build-deps curl gnupg gcc g++ libc-dev libffi-dev libxml2 musl-dev unixodbc unixodbc-dev \
    && curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.6.1.1-1_amd64.apk \
    && curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.6.1.1-1_amd64.sig \
    && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --import - \
    && gpg --verify msodbcsql17_17.6.1.1-1_amd64.sig msodbcsql17_17.6.1.1-1_amd64.apk \
    && echo y | apk add --allow-untrusted --no-cache msodbcsql17_17.6.1.1-1_amd64.apk \
    && pip install -U pip -r /tmp/requirements.txt \
    && apk del --no-cache .build-deps

RUN apk add --no-cache tini

RUN echo '0 21 * * * python /src/tasks_on_time.py' >> /etc/crontabs/root

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/usr/sbin/crond", "-f"]
