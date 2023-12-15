FROM python:3.11.5

WORKDIR /color_recognition

COPY requirements.txt /color_recognition/
RUN pip install -r requirements.txt
COPY .  .

ENV FLASK_APP=color_recognition.py
ENV FLASK_DEBUG=1
ENV FLASK_CONFIG='production'

EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]