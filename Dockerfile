FROM debian:stable

## Set time zone from env in docker container
RUN date

## For geckodriver installation: curl/wget/libgconf/unzip
RUN apt-get update -y && apt-get install -y wget curl unzip libgconf-2-4

## Installing Firefox to Debian Stretch https://unix.stackexchange.com/a/406554/169768
RUN sh -c 'echo "APT::Default-Release "stable";" >> /etc/apt/apt.conf' 
RUN sh -c 'echo "deb http://ftp.hr.debian.org/debian sid main contrib non-free" >> /etc/apt/sources.list'
RUN apt-get update -y && apt-get install -yt sid firefox
RUN apt-get update -y && apt-get install -y xvfb python3 python3-pip 


# Download, unzip, and install geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'`/geckodriver-`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'`-linux64.tar.gz
RUN tar -zxf geckodriver-`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'`-linux64.tar.gz -C /usr/local/bin
RUN chmod +x /usr/local/bin/geckodriver


COPY requirements.txt .
RUN pip3 install -r requirements.txt


# Set display port and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

COPY ./run.sh /

# Bash script to invoke xvfb, any preliminary commands, then invoke project
RUN sed -i 's/\r$//g' /run.sh && chmod +x /run.sh

WORKDIR /app