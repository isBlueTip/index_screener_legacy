FROM python:3.10.9-slim

LABEL application="screener"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update \
    && apt install -y python3-dev \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/* \

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip \
  && pip3 install -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]