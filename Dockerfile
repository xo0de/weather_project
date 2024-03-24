FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install Flask && pip install requests && pip install python-dotenv

EXPOSE 5000

CMD ["python", "main.py"]

