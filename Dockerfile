FROM python:3-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --upgrade --no-cache-dir -r requirements.txt

COPY ./app /app

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0" ]
