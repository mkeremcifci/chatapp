import json
import socket
import threading
import json
import requests

host = "127.0.0.1"
port = 12345


BASE_URL = "http://127.0.0.1:8000"
TOKEN_URL = f"{BASE_URL}/token"


def handleClinet(clientSocket : socket, addr):
    print(f"{addr} ile bağlantı kuruldu.")
    try:
        while True:
            message = clientSocket.recv(1024).decode("utf-8")
            if not message:
                break


            try:
                data = json.loads(message)
                print(f"Gelen veri: {data}")


                username = data.get("username")
                password = data.get("password")



                if username and password:
                    responseApi = requests.post(
                        TOKEN_URL,
                        json=data,
                    )
                    if responseApi.status_code == 200:
                        token = responseApi.json().get("access_token")
                        print(f"Token: {token}")
                        clientSocket.send(token.encode("utf-8"))
                    else:
                        print(f"Token alınamadı {responseApi.status_code} - {responseApi.text}")
                        response = "Token alınamadı"
                        clientSocket.send(response.encode("utf-8"))

                else:
                    response = json.dumps({"status": "error", "message": "Eksik veri: username veya password yok!"})
                    clientSocket.send(response.encode("utf-8"))
            except json.JSONDecodeError:
                response = json.dumps({"status": "error", "message": "Geçersiz JSON formatı!"})
                clientSocket.send(response.encode("utf-8"))

    except Exception as e:
        print(f"Hata: {e}")
    finally:
        clientSocket.close()




def startServer(host, port):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((host,port))
    serverSocket.listen(5)
    print(f"Sunucu {host}:{port} üzerinde çalışıyor")

    while True:
        clinetSocket, addr = serverSocket.accept()
        handleClinet(clientSocket=clinetSocket, addr=addr)

startServer(host, port)


