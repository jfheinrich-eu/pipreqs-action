FROM python:3.13.3-alpine3.21

COPY LICENSE README.md entrypoint.sh /

RUN apk add --no-cache git
RUN apk add --no-cache python3 py3-pip
RUN pip3 install pipreqs

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
