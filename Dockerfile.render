FROM python:3.10.7-slim-bullseye
# RUN chmod 777 /template
# python3.10 -m venv venv && . ./venv/bin/activate
ENV VIRTUAL_ENV=/opt/venv
RUN python3.10 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /template
ENV TZ=Asia/Kolkata PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
RUN apt-get update && apt-get upgrade -y
RUN python3.10 -m pip install -U pip
RUN pip3 install -U setuptools wheel
RUN apt-get install -y wget curl bash neofetch git sudo
RUN sudo apt-get install -y apt-utils build-essential
RUN apt-get install python3-dev -y
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt
RUN rm -rf requirements.txt
RUN apt-get update && apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
CMD ["python3.10", "main.py"]
