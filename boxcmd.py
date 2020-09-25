
import grpc
import gcommand_pb2_grpc
import gcommand_pb2



class BoxCmd():

    def __init__(self):
        channel = grpc.insecure_channel('boxdb_boxcmd_1:50051')
        self.stub = gcommand_pb2_grpc.RemoteCommandStub(channel)

    def exec_cmd(self, box):
        if box.get('ssid'):
            cmd = gcommand_pb2.Command(boxname=box['name'],
                                       command='ssid',
                                       params=box['ssid'])
            rc = self.stub.ExecCommand(cmd)
        if box.get('macs'):
            cmd = gcommand_pb2.Command(boxname=box['name'],
                                       command='macs',
                                       params=" ".join(box['macs']))
            rc = self.stub.ExecCommand(cmd)
