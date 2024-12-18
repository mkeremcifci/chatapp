import requests
from tkinter import messagebox

BASE_URL = "http://127.0.0.1:8000"
TOKEN_URL = f"{BASE_URL}/token"
data = {
    "username":None,
    "password":None
}
def handleLogin(username, password):
    data["username"] = username
    data["password"] = password
    response = requests.post(
        TOKEN_URL,
        json=data,
    )
    if response.status_code == 200:
        token = response.json().get("access_token")
        print(f"Token:{token}")
        return token
    else:
        print(f"Token alınamadı {response.status_code} - {response.text}")
        return None



