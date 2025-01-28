FROM python:3.7.0

WORKDIR /app

COPY app/ /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]