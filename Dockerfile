FROM python:3.9 as builder

# Build bot
WORKDIR /opt/lib
COPY . /opt/lib

RUN pip install fastapi

ENTRYPOINT ["python", "main.py"]
EXPOSE 4000