import requests
import os

url = "http://localhost:5000/subredes"

value = int(os.getenv('VALUE', 0))

print(f"VALUE: '{value}'")

endereco_ip = "192.168.247.119"
mascara = "/24"

dados = {
    "endereco_ip": endereco_ip,
    "mascara": mascara
}

response = requests.post(url, json=dados)

print("Status:", response.status_code)

if response.ok:
    print(response.json())
else:
    print("Erro:", response.text)