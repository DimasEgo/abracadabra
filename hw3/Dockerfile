FROM python:3.10

ENV APP_HELPER /app

WORKDIR $APP_HELPER

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
