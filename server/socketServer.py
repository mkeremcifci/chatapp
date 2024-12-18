import socket
import threading






def startServer(host, port):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((host,port))
    serverSocket.listen(5)
    print(f"Sunucu {host}:{port} üzerinde çalışıyor")

    while True:
        clinetSocket, addr = serverSocket.accept()



