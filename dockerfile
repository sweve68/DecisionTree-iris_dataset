FROM python:3.9

WORKDIR /app

COPY . .

EXPOSE 8000

RUN pip install fastapi

CMD ["python","main.py",]