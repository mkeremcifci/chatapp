import socket
import json

data = {
    "username":"Kerem",
    "password":"password"
}

def startClinet():
    serverHost = "127.0.0.1"
    serverPort = 12345

    try:
        clinetSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        clinetSocket.connect((serverHost, serverPort))
        print("Servera bağlanıldı")

        jsonData = json.dumps(data)
        clinetSocket.send(jsonData.encode("utf-8"))
        print("Data gönderildi")
        response = clinetSocket.recv(1024).decode("utf-8")
        print(f"Sunucudan gelen yanıt:{response}")

    except Exception as e:
        print(f"Hata oluştu{e}")

    finally:
        clinetSocket.close()

startClinet()