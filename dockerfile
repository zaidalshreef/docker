FROM python:3.7.12-buster

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0:8080"]
