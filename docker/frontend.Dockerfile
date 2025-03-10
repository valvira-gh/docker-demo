FROM python:3.13.2

WORKDIR /app
COPY ../frontend /app
RUN pip install flask requests

CMD ["python", "app.py"]
