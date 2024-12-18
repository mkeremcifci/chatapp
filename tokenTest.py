import requests

BASE_URL = "http://127.0.0.1:8000"
TOKEN_URL = f"{BASE_URL}/token"
VERIFY_TOKEN_URL = f"{BASE_URL}/verify-token"

data = {
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIn0.pHaus62nD9DrNbTCRTVOOhnRbbXZnL031tfLEk_qP5s"
}

while True:
    a = int(input("a:"))
    if a == 1:
        response = requests.post(
            TOKEN_URL,
            json={"username":"Kerem", "password":"password"}
        )
        if response.status_code == 200:
            data["token"] = response.json().get("access_token")
            print(f"Token: {data["token"]}"),
        else:
            print(f"Token alınamadı. Hata {response.status_code} - {response.text}")
    if a == 2:
        response = requests.post(
            VERIFY_TOKEN_URL,
            json=data,
        )
        if response.status_code == 200:
            id = int(response.json().get("user_id"))
            print(f"Id: {id}")
        else:
            print(f"Hata {response.status_code} - {response.text}")
        
        
        