<!-- HERO -->
<div align="center">

<img src="https://brands.home-assistant.io/homeassistant/icon@2x.png" alt="Home Assistant" width="110">

# Home Lab

**Self-hosted  homelab on Raspberry Pi and Orange Pi.**

![Home Assistant](https://img.shields.io/badge/Home_Assistant-41BDF5?style=flat-square&logo=home-assistant&logoColor=white)
![Pi-hole](https://img.shields.io/badge/Pi--hole-96060C?style=flat-square&logo=pi-hole&logoColor=white)
![WireGuard](https://img.shields.io/badge/WireGuard-88171A?style=flat-square&logo=wireguard&logoColor=white)
![Nextcloud](https://img.shields.io/badge/Nextcloud-0082C9?style=flat-square&logo=nextcloud&logoColor=white)
![Jellyfin](https://img.shields.io/badge/Jellyfin-00A4DC?style=flat-square&logo=jellyfin&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu_Server-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Apache](https://img.shields.io/badge/Apache-F28C28?style=flat-square&logo=apache&logoColor=white)
<br>
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi_5-A22846?style=flat-square&logo=raspberry-pi&logoColor=white)
![Orange Pi](https://img.shields.io/badge/Orange_Pi-FF7F00?style=flat-square)
<br>

</div>

## ✨ What is this?

A small self-hosted homelab built with a Raspberry Pi 5 and an Orange Pi 3B, running Home Assistant, Docker services, MQTT, Pi-hole and WireGuard.

## 🧱 The stack
### Raspberry Pi 5

- **Home Assistant OS**

- Home automation, networking and device management.

- 8 GB RAM · 512 GB SSD

| Service | Role |
| :--- | :--- |
| **Home Assistant** | Automation & state engine |
| **Mosquitto** | MQTT broker |
| **ESPHome** | ESP device integration |
| **Pi-hole** | Network-wide DNS filtering |
| **WireGuard** | VPN & remote access |

---

### Orange Pi 3B

- **Ubuntu Server**

- Secondary server for fan control and containerized services.

- 8 GB RAM · 512 GB SSD

| Service | Role |
| :--- | :--- |
| **Fan Control** | MQTT-based fan control script |
| **Portainer** | Docker container management |
| **Nextcloud** | Self-hosted files, calendar & contacts |
| **Jellyfin** | Self-hosted media server |
| **MariaDB** | Database |
| **Redis** | Cache & data store |



## 🗺️ How it connects

<div align="center">

<img src="img/map.svg" alt="Home Lab network diagram" width="900">

</div>

## 💡 Devices

| | Device | Location | Link | Role |
|:-:|:--|:--|:--|:--|
| 💡 | Double Smart Switch | Bedroom Lights | Tuya Wifi | On/Off |
| 💡 | Smart Leds | Desktop Leds | Tuya/Wifi | On/Off, RGBW |
| 🔌 | Smart Plug | Additional Power | Tuya/Wifi | On/Off |
| 🔌 | Smart Power Strip | Desktop Power | Tuya/Wifi | On/Off |
| 🖥️ | Desktop PC  | Desktop | MQTT | On/Off, Commands |

## ⚙️ Most Important Automations

- **GPS Shutdown Desktop PC** — Triggers an MQTT shutdown of the PC and associated smart plugs based on mobile GPS presence, with action notification.
- **Orange Pi Fan Control** - Publishes temperature data via MQTT; Home Assistant controls two fans based on temperature thresholds.
## 💵 Cost

<table width="80%">
  <thead>
    <tr>
      <th>Category</th>
      <th>Component</th>
      <th>Cost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2"><b>Hardware</b></td>
      <td>Raspberry Pi 5 (8 GB)</td>
      <td>117.00 €</td>
    </tr>
    <tr>
      <td>Orange Pi 3B (8 GB)</td>
      <td>56.39 €</td>
    </tr>
    <tr>
      <td rowspan="5"><b>Power & Cooling</b></td>
      <td>Raspberry Pi Power Supply</td>
      <td>15.47 €</td>
    </tr>
    <tr>
      <td>Orange Pi Power Supply ×2</td>
      <td>20.78 €</td>
    </tr>
    <tr>
      <td>SSD Heatsinks ×2</td>
      <td>11.98 €</td>
    </tr>
    <tr>
      <td>5v Fans ×2</td>
      <td>2.98 €</td>
    </tr>
    <tr>
      <td>UPS</td>
      <td>41.99 €</td>
    </tr>
    <tr>
      <td rowspan="6"><b>Storage & Accessories</b></td>
      <td>Raspberry Pi SSD (512 GB)</td>
      <td>Reused</td>
    </tr>
    <tr>
      <td>Orange Pi SSD (512 GB)</td>
      <td>Reused</td>
    </tr>
    <tr>
      <td>PCIe M.2 Adapter</td>
      <td>16.00 €</td>
    </tr>
    <tr>
      <td>Self Made Control Fan PCB</td>
      <td>3.00 €</td>
    </tr>
    <tr>
      <td>Raspberry Pi Case</td>
      <td>12.96 €</td>
    </tr>
    <tr>
      <td>Orange Pi Case</td>
      <td>9.83 €</td>
    </tr>
    <tr>
      <td colspan="2"><b>Total</b></td>
      <td><b>307.38 €</b></td>
    </tr>
  </tbody>
</table>

## Explanations

### 🌀 Orange Pi Fan Control Script

A small Python script running on the Orange Pi 3B that connects it to Home Assistant through MQTT. It lets Home Assistant turn the two fans on and off, and it sends system data back so Home Assistant can decide when to do it.

- **Fan control:** the fans are wired to two GPIO pins. The script turns them on at startup and then follows the on/off commands it receives over MQTT.
- **Telemetry:** every 5 seconds it publishes the CPU and NVMe temperatures, CPU usage, RAM usage, used disk space and uptime.
- **Availability:** the Orange Pi reports `Online` or `Offline`, so Home Assistant knows if it is reachable.
- **Remote reboot:** the board can be restarted with an MQTT message.
- **Logic in Home Assistant:** the script only executes orders. The temperature thresholds that decide when the fans turn on or off are set in Home Assistant.

**Requirements:** Python 3, `paho-mqtt`, `psutil`, and root permissions to control the GPIO pins.

## 🐳 Docker Services on the Orange Pi

The Orange Pi runs three containers defined in a single Docker Compose file. They all restart automatically after a reboot or a power cut.

- **Jellyfin** — Self-hosted media server for movies and TV shows. The library folders and the configuration are stored on the Orange Pi's SSD, so nothing is lost if the container is updated or recreated. Available on port `8096`.
- **Portainer** — Web interface to manage all the Docker containers without using the terminal: start, stop, update and check logs. Available on port `9443` over HTTPS.
- **Nextcloud** — Private cloud for files, calendar and contacts. It uses a MariaDB database and is served over HTTPS with a self-signed certificate, so the connection is encrypted inside the local network. Available on ports `8080` (HTTP) and `8443` (HTTPS).

**Storage:** media and configuration files are saved in folders on the Orange Pi. Nextcloud data and Portainer settings are kept in Docker volumes, so they survive updates.

**Network:** Nextcloud runs on its own Docker network so it can talk to the database container without exposing it to the rest of the network.

<br>
<div align="center">
  <p style="font-size: 14px">
    Licensed under the <b>MIT License</b> · <a href="LICENSE">View license</a>
  </p>
</div>