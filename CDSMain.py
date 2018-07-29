import socket
import random

print("RDA-Bot ContentDeliverySystem Started")
print("! Please visit www.sunrobindev.de")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
server_socket.bind(('185.249.199.220', 1338)) #Bind socket to IP and port
server_socket.listen(1) #Backlog (number) defines max. clients
while True:
    (client_socket, addr) = server_socket.accept()#accept Connction
    msg = client_socket.recv(1024)
    print("requested " + str(msg, "utf8"))
    if str(msg, "utf8") == "gamingsong":
        file = open('gamingsongs.txt',mode='r')
        song = file.readlines()
        file.close()
        title = random.choice(song)
        print("suggested: " + title)
        client_socket.send(bytes(title, "utf8"))
