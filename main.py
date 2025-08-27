import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SUNAT_CLIENT_ID")
CLIENT_SECRET = os.getenv("SUNAT_CLIENT_SECRET")
USUARIO_SOL = os.getenv("SUNAT_USUARIO_SOL")
CLAVE_SOL = os.getenv("SUNAT_CLAVE_SOL")

def get_token_auth():
    url = f"https://api-seguridad.sunat.gob.pe/v1/clientessol/{CLIENT_ID}/oauth2/token/"
    data = {
        "grant_type": "password",
        "scope": "https://api-sire.sunat.gob.pe",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "username": f"{USUARIO_SOL}",
        "password": CLAVE_SOL,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(url, data=data, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    token_response = get_token_auth()
    print("Response login")
    print(token_response)
