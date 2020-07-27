FROM python:3.8.2-buster

EXPOSE 5000/tcp

RUN adduser boxdb

WORKDIR /home/boxdb

USER boxdb:boxdb

RUN pip install --no-cache-dir \
        Flask==1.1.2 \
        Flask-RESTful==0.3.8

COPY --chown=boxdb:boxdb . .

CMD ["python", "main.py"]
