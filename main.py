import requests
import os

ip = input("Enter the IP address: ")
url = f"https://ipinfo.io/{ip}/json"

response = requests.get(url)
data = response.json()
coords = data['loc'].split(',')

os.system('cls' if os.name == 'nt' else 'clear')

print(f"Ip address: {ip}")
print("-------------------------")
print(f"City: {data['city']}")
print(f"Region: {data['region']}")
print(f"Country: {data['country']}")
print(f"Coords: {coords[0]}, {coords[1]}")
print(f"Postal: {data['postal']}")
print(f"Timezone: {data['timezone']}")
print(f"Organisation: {data['org']}")
print(f'Google Maps: https://www.google.com/maps/?q={coords[0]},{coords[1]}')