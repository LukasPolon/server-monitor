#########################################
## Dockerfile for the server-monitor project.
##
## Run for development:
##      - docker run -it -v /proc:/server-stats -v $(pwd):/server-monitor s_monitor:test001 /bin/bash
#########################################
FROM alpine

ADD . /server-monitor
WORKDIR /server-monitor

# Run python as: python3, and pip as: pip3
RUN apk add bash python3 python3-dev gcc musl-dev
RUN pip3 install --upgrade pip
RUN pip3 install -U setuptools
