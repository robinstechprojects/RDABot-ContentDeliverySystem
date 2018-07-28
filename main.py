import socket
import threading

print("RDA - ContenDeliverySystem started !")
print("! Please Visit www.sunrobindev.de !")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
server_socket.bind(('127.0.0.1', 1338)) #Bind socket to IP and port
server_socket.listen(2) #Backlog (number) defines max. clients

class Fred(threading.Thread):
    def __init__(self, iD, client_socket):
        threading.Thread.__init__(self)
        self.iD = iD
        self.client_socket = client_socket

    def run(self):
        while True:
            msg = client_socket.recv(1024)
            print(str(msg, "utf8")) #recive from client


while True:
    (client_socket, addr) = server_socket.accept() #accept connection
    ct1 = Fred(1, client_socket)
    ct1.start()
