FROM ubuntu:14.04

ADD . /src
RUN apt-get -y update && apt-get install -y python3-pil python3-aalib

USER nobody

ENTRYPOINT ["/usr/bin/python3", "/src/aaconvert.py"]
