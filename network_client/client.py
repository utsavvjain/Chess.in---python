from network_client.config import Configuration
from network_common.wrappers import Response,Request
import sys
import socket
class NetworkClient :
    def __init__(self):
        self.server_configuration=Configuration()
        self.server_configuration._validate_values()
        if self.server_configuration.has_exceptions: 
            for exception in self.server_configuration.exceptions.values() :
                print(exception[1])
            sys.exit() #nrerd to be coverted to code that raises exception
    def send(self,request) :
        client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((self.server_configuration.host,self.server_configuration.port)) 
        request_data=request.to_json()
        client_socket.sendall(bytes(str(len(request_data)).ljust(1024),"utf-8"))
        client_socket.sendall(bytes(request_data,"utf-8"))
        data_bytes=b''
        to_receive=1024
        while len(data_bytes)<to_receive :
            dbytes=client_socket.recv(to_receive-len(data_bytes))
            data_bytes+=dbytes
        response_data_length=int(data_bytes.decode("utf-8")) 
        data_bytes=b''
        to_receive=response_data_length
        while len(data_bytes)<to_receive :
            dbytes=client_socket.recv(to_receive-len(data_bytes))
            data_bytes+=dbytes
        response_data=data_bytes.decode("utf-8")
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()
        response=Response.from_json(response_data)
        return response      
      