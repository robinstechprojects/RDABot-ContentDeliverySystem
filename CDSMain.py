import socket
import random
from bs4 import BeautifulSoup
import requests

print("RDA-Bot ContentDeliverySystem Started")
print("! Please visit www.sunrobindev.de !")
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
    elif str(msg, "utf8") == "rapsong":
        file = open('rapsongs.txt',mode='r')
        song = file.readlines()
        file.close()
        title = random.choice(song)
        print("suggested: " + title)
        client_socket.send(bytes(title, "utf8"))
    elif str(msg, "utf8") == "nightcore":
        file = open('nightcore.txt',mode='r')
        song = file.readlines()
        file.close()
        title = random.choice(song)
        print("suggested: " + title)
        client_socket.send(bytes(title, "utf8"))
    elif str(msg, "utf8") == "metalsong":
        file = open('metalsongs.txt',mode='r')
        song = file.readlines()
        file.close()
        title = random.choice(song)
        print("suggested: " + title)
        client_socket.send(bytes(title, "utf8"))
    elif str(msg, "utf8") == "rocksong":
        file = open('rocksongs.txt',mode='r')
        song = file.readlines()
        file.close()
        title = random.choice(song)
        print("suggested: " + title)
        client_socket.send(bytes(title, "utf8"))
    elif str(msg, "utf8") == "wisdom":
        file = open('wisdoms.txt',mode='r')
        song = file.readlines()
        file.close()
        title = random.choice(song)
        print("suggested: " + title)
        client_socket.send(bytes(title, "utf8"))
    elif str(msg, "utf8") == "tweetrequest":
        msg2 = client_socket.recv(1024)
        url = 'https://www.twitter.com/'+str(msg2, "utf8")
        r = requests.get(url)
        soup =  BeautifulSoup(r.content, "lxml")
        f = soup.find('li', class_="ProfileNav-item--followers")
        title = f.find('a')['title']
        print("title")
        client_socket.send(bytes(title, "utf8"))
