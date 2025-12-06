# telemetria.py
# Programa para envío automático de datos de temperatura a ThingsBoard
 
import requests
import random
import time

# Cargar token desde archivo externo
with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

# URL de ThingsBoard demo
URL = f"https://demo.thingsboard.io/api/v1/{TOKEN}/telemetry"

# Loop infinito de envío automático
while True:
    # Temperatura aleatoria entre 18 y 32
    temp = round(random.uniform(18, 32), 2)
    data = {"temperature": temp}

    try:
        requests.post(URL, json=data, timeout=3)
        print(f"Enviado: {data}")
    except Exception as e:
        print("Error:", e)

    # Esperar 5 segundos (ajustable)
    time.sleep(5)