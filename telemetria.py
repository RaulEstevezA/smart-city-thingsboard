import requests
import random
import time

with open("token.txt", "r") as f:
    TOKEN = f.read().strip()
URL = f"http://thingsboard.cloud/api/v1/{TOKEN}/telemetry"

while True:
    temp = round(random.uniform(18, 32), 2)
    data = {"temperature": temp}

    try:
        requests.post(URL, json=data, timeout=3)
        print(f"Enviado: {data}")
    except Exception as e:
        print("Error:", e)

    time.sleep(3)