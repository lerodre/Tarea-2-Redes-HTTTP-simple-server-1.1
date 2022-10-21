FROM ubuntu

MAINTAINER lerodre

RUN apt-get update
RUN apt install python3 -y
RUN apt install git -y
RUN apt install pip -y
RUN python3 -m pip install requests
RUN apt install net-tools
WORKDIR app/
RUN git clone https://github.com/psf/requests.git
COPY app.py app.py

#CMD ifconfig	#si se descomenta esta linea, comenta el entrypoint, hacer un BUILD y despues un RUN de la imagen cliente.

CMD ["python3","/app/app.py"]
