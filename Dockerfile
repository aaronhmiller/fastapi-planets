FROM python:3-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --upgrade --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--reload"]
#ENTRYPOINT [ "python3 -m uvicorn app.main:app" ]
