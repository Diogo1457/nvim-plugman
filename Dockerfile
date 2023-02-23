FROM ubuntu

RUN mkdir -p /nvim_plugman/src
COPY src /nvim_plugman/src
WORKDIR /nvim_plugman/src
RUN apt update
RUN apt install -y python3 curl git npm
RUN useradd -m test 
USER test
