# Tarea-2-Redes-HTTTP-simple-server-1.1
Obtener el trafico request de un servidor http simple, con ayuda de python, c++, docker, y Wireshark en Linux Ubuntu 22.04lt.

## Informacion general
El proposito de este trabajo es generar trafico HTTP para capturarlo con un sniffer.

## Setup
-Hay que tener en cuenta que se necesita usar los repositorios http request (https://github.com/psf/requests) y http simple server (https://github.com/trungams/http-server).

Sofware necesario:
- Wireshark u otro sniffer
- Docker
Sofware opcional:
- Net-tools (facilita la busqueda de direcciones ip).

Lo demás se hace el clone del repositorio para obtener las carpetas de dockerfile server y cliente.

## Uso
1) Abrir sniffer, y empezar a capturar en la interfaz de red Docker0.
2) Armar el docker servidor, `sudo docker build -t server:1.0 (RUTA Dockerfile carpeta dockerfileserver)`. Después hacer un run de la imagen docker creada, este empezará a hostear un server en el primer ip disponible de la LAN.
3) Conseguir ip del docker imagen del servidor, abrir carpeta dockerfile, editar app.py, remplazando el ip actual en la segunda lina con el ip del servidor.
4) Abrir otro terminal, y armar dockerfile cliente, `sudo docker build -t cliente:1.0 (RUTA Dockerfile carpeta dockerfile)`. Después hacer un run de la imagen cliente creada. Si este funcionó, imprime en terminal Hello world.
5) Revisar captura de sniffer.


