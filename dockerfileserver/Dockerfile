FROM ubuntu

MAINTAINER lerodre

RUN apt-get update
RUN apt install net-tools
RUN apt install python3 -y
RUN apt install pip -y
RUN apt install build-essential manpages-dev
RUN apt install git -y
RUN apt install cmake -y
RUN git clone https://github.com/trungams/http-server.git
WORKDIR /app
RUN cmake /http-server
RUN make

#CMD ifconfig	#si se descomenta esta linea, comenta el entrypoint, hacer un BUILD y despues un RUN de la imagen servidor.

ENTRYPOINT ["./SimpleHttpServer"]
