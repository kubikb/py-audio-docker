FROM continuumio/miniconda

WORKDIR /usr/src/app

COPY requirements.txt ./

# Install gcc and libav-tools
RUN apt-get install -y gcc libav-tools

# Install requirements
RUN pip install -r requirements.txt

# Testing resources
COPY test/ test/.