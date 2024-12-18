from server.socketServer import startServer
from server.config import HOST, PORT


if __name__ == "__main__":
    print("Sunucu başlatılıyor")
    startServer(HOST, PORT)
