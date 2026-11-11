# TP N.º 4 – Trabajo Práctico Integrador
## Redes de Computadoras (3643)

**Universidad Nacional de La Matanza**  
**Grupo: 15**  
**Año:** 2026

---

## 1. Descripción del proyecto

Este repositorio tiene los scripts de Python suministrados por la cátedra.

Los programas permiten obtener información de los dispositivos de red y los hosts detectados por el controlador, facilitando la consulta y el procesamiento del inventario de la infraestructura.

## 2. Estructura del repositorio

```
api-python-redes-cisco/
│
├── src/
│   ├── 01_get-ticket.py
│   ├── 02_get-network-device.py
│   ├── 03_get-host.py
│   ├── 04_tabulate.py
│   └── 05_script_propio.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 3. Descripción de los scripts

### 3.1. Scripts suministrados por la cátedra

**01_get-ticket.py – Autenticación**

Realiza una petición POST al endpoint `/api/v1/ticket` para autenticar al usuario y obtener un Service Ticket. Este ticket permite autorizar las consultas posteriores a la API REST del Network Controller.

**02_get-network-device.py – Consulta de dispositivos**

Realiza una petición GET al endpoint `/api/v1/network-device` para obtener información de los dispositivos de red registrados en el controlador. Presenta datos como el nombre del equipo, identificador de plataforma y dirección IP de administración.

**03_get-host.py – Consulta de hosts**

Realiza una petición GET al endpoint `/api/v1/host` para recuperar los hosts detectados por el Network Controller. Obtiene información como nombre, tipo de dispositivo, dirección IP, dirección MAC e interfaz de conexión.

**04_tabulate.py – Visualización de inventario**

Consulta los dispositivos de red y los hosts mediante la API REST y utiliza la biblioteca `tabulate` para presentar los resultados en tablas organizadas y legibles por consola.

### 3.2. Script desarrollado por el grupo

**05_script_propio.py – Exportación del inventario a archivos CSV**

El script realiza una autenticación en el Network Controller mediante una petición POST al endpoint `/api/v1/ticket`, solicitando al usuario sus credenciales y obteniendo un nuevo Service Ticket para autorizar las consultas.

Posteriormente, realiza dos peticiones GET a los endpoints `/api/v1/network-device` y `/api/v1/host` para recuperar la información de los dispositivos de red y los hosts detectados por el controlador.

Finalmente, procesa las respuestas JSON y exporta los resultados a dos archivos CSV:

- **dispositivos_red.csv:** contiene el nombre del dispositivo, identificador de plataforma, dirección IP de administración, versión de software y estado de recolección.
- **hosts.csv:** contiene el nombre del host, tipo de dispositivo, dirección IP, dirección MAC, interfaz de conexión y estado de ping.

El programa informa los códigos de estado HTTP, comprueba las respuestas recibidas y muestra la cantidad de dispositivos y hosts exportados.