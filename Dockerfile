FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install Flask && pip install requests

EXPOSE 5000

CMD ["python", "main.py"]

