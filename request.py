import requests

BASE_URL = "http://127.0.0.1:8000"
TOKEN_URL = f"{BASE_URL}/token"

data = {
    "username": "kerem",
    "password": "password"
}

def getToken():
    response = requests.post(
        TOKEN_URL,
        json=data,
    )
    if response.status_code == 200:
        token = response.json().get("access_token")
        print(f"Token: {token}")
        return token
    else:
        print(f"Token alınamadı {response.status_code} - {response.text}")
        return None

getToken()