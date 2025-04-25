FROM ubuntu:25.04

ENV TZ="America/Sao_Paulo"

RUN apt-get update

RUN apt-get install -y tzdata

RUN dpkg-reconfigure --frontend noninteractive tzdata

COPY logs.sh /logs.sh
RUN chmod +x /logs.sh

CMD ["/logs.sh"]