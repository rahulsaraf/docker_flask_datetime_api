# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.5
COPY . /app
WORKDIR /app
ENV FLASK_APP=app.py
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
