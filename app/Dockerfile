FROM python:3.12.2

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./ .

CMD [ "fastapi", "dev", "./main.py", "--host", "0.0.0.0", "--port", "80"]