import socket

print("RDA - ContenDeliverySystem started !")
print("! Please Visit www.sunrobindev.de !")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
server_socket.bind((socket.gethostname(), 1337)) #Bind socket to IP and port
server_socket.listen(1) #Backlog (number) defines max. clients
while True:
    (client_socket, addr) = server_socket.accept() #accept connection
    msg = client_socket.recv(1024)
    print(str(msg, "utf8")) #recive from client
