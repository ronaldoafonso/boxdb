FROM python:3.8.2-buster

EXPOSE 30000/tcp

RUN adduser boxdb

WORKDIR /home/boxdb

USER boxdb:boxdb

RUN pip install --no-cache-dir \
        Flask==1.1.2 \
        Flask-RESTful==0.3.8 \
        pymongo==3.11.0 \
#       grpcio-tools==1.1.0 \
        pylint==2.8.2

COPY --chown=boxdb:boxdb ./gcommand ./gcommand/

#RUN python -m grpc_tools.protoc \
#           -I=./gcommand \
#           --python_out=./gcommand \
#           --grpc_python_out=./gcommand \
#           ./gcommand/gcommand.proto

COPY --chown=boxdb:boxdb *.py ./

CMD ["python", "main.py"]
