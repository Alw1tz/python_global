import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"

response = requests.get(url)

print(response.status_code)
if response.status_code == 200:
    data = response.json()
    print(f"Información sobre {data['name']}:")
    print(f"ID: {data['id']}")
    print(f"Altura: {data['height']}")
    print(f"Peso: {data['weight']}")
else:
    print("Error al hacer la solicitud")