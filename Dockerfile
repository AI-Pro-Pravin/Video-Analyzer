FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt && apt-get update && apt-get install -y ffmpeg
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT new:new