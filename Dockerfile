FROM python:3.8.2-buster

EXPOSE 5000/tcp

RUN adduser boxdb

WORKDIR /home/boxdb

USER boxdb:boxdb

RUN pip install --no-cache-dir flask==1.1.2

COPY --chown=boxdb:boxdb . .

CMD ["python", "main.py"]
