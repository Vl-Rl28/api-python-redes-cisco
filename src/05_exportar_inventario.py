
import csv
import requests
from getpass import getpass

base_url = "http://localhost:58000/api/v1"

# 1. Autenticación en el Network Controller
username = input("Usuario: ")
password = getpass("Contraseña: ")

ticket_response = requests.post(
    base_url + "/ticket",
    json={
        "username": username,
        "password": password
    }
)

print("Estado de autenticación:", ticket_response.status_code)
ticket_response.raise_for_status()

ticket = ticket_response.json()["response"]["serviceTicket"]

headers = {"X-Auth-Token": ticket}

# 2. Obtener los dispositivos de red
devices_response = requests.get(
    base_url + "/network-device",
    headers=headers
)

print("Estado de consulta de dispositivos:", devices_response.status_code)
devices_response.raise_for_status()

devices = devices_response.json()["response"]

# 3. Obtener los hosts
hosts_response = requests.get(
    base_url + "/host",
    headers=headers
)

print("Estado de consulta de hosts:", hosts_response.status_code)
hosts_response.raise_for_status()

hosts = hosts_response.json()["response"]

# 4. Exportar los dispositivos a CSV
device_columns = [
    "hostname",
    "platformId",
    "managementIpAddress",
    "softwareVersion",
    "collectionStatus"
]

exported_devices = [
    {column: device.get(column, "") for column in device_columns}
    for device in devices
    if device.get("hostname")
]

with open("dispositivos_red.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=device_columns)
    writer.writeheader()
    writer.writerows(exported_devices)

# 5. Exportar los hosts a CSV
host_columns = [
    "hostName",
    "hostType",
    "hostIp",
    "hostMac",
    "connectedInterfaceName",
    "pingStatus"
]

exported_hosts = [
    {column: host.get(column, "") for column in host_columns}
    for host in hosts
]

with open("hosts.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=host_columns)
    writer.writeheader()
    writer.writerows(exported_hosts)

# 6. Mostrar el resultado
print("\nExportación completada correctamente.")
print("Dispositivos exportados:", len(exported_devices))
print("Hosts exportados:", len(exported_hosts))
print("Archivos generados: dispositivos_red.csv y hosts.csv")
