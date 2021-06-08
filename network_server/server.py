from network_server.config import Configuration
from network_common.wrappers import Request,Response
import socket
import sys
from threading import Thread
class RequestProcessor(Thread):
    def __init__(self,client_socket,requestHandler) :
        self.client_socket=client_socket
        self.requestHandler=requestHandler
        Thread.__init__(self) 
        self.start()
    def run(self) :
        to_receive=1024
        data_bytes=b''
        while len(data_bytes)<to_receive :
            bytes_read=self.client_socket.recv(to_receive-len(data_bytes))
            data_bytes+=bytes_read
        request_data_length=int(data_bytes.decode('utf-8'))             
        to_receive=request_data_length
        data_bytes=b''
        while len(data_bytes)<to_receive :
            bytes_read=self.client_socket.recv(to_receive-len(data_bytes))
            data_bytes+=bytes_read
        request_data=data_bytes.decode('utf-8')
        request=Request.from_json(request_data)
        response=self.requestHandler(request)
        response_data=response.to_json()
        self.client_socket.sendall(bytes(str(len(response_data)).ljust(1024),'utf-8') )
        self.client_socket.sendall(bytes(response_data,'utf-8'))   
        self.client_socket.close()
  
class NetworkServer:
    def __init__(self,requestHandler) :
        self.server_configuration=Configuration()
        self.requestHandler=requestHandler 
        self.server_configuration._validate_values
        if self.server_configuration.has_exceptions :
            for exception in self.server_configuration.exceptions.values() : print(exception)
            sys.exit()
    def start(self) :
        server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.bind((self.server_configuration.host,self.server_configuration.port))
        server_socket.listen()
        print(f"Server is ready and is listening on port :",self.server_configuration.port)
        while True :
            client_socket,client_name=server_socket.accept()
            request_processor=RequestProcessor(client_socket,self.requestHandler) 
        server_socket.close()  
