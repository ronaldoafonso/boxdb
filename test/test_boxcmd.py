
from concurrent import futures

import grpc
import gcommand_pb2_grpc
import gcommand_pb2


def check_request(request):
    if request.boxname == "":
        return True
    return False
#       (request.command == "ssid" or request.command == "macs") and
#       (request.params == "z3n" or request.params == "11:22:33:44:55:66":
#        paramOK = True

class RemoteCommandService(gcommand_pb2_grpc.RemoteCommandServicer):

    def ExecCommand(self, request, context):
        if check_request(request):
            return gcommand_pb2.ReturnMsg(returnMsg="Error: request error.")
        return gcommand_pb2.ReturnMsg(returnMsg="Ok")


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gcommand_pb2_grpc.add_RemoteCommandServicer_to_server(
        RemoteCommandService(),
        server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server()
