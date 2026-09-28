<!-- HERO -->
<div align="center">

<img src="https://brands.home-assistant.io/homeassistant/icon@2x.png" alt="Home Assistant" width="110">

# Home Lab

**A self-hosted smart home & homelab on Raspberry Pi and Orange Pi.**
*Local-first · Zigbee · WireGuard · Config as code*

![Home Assistant](https://img.shields.io/badge/Home_Assistant-41BDF5?style=flat-square&logo=home-assistant&logoColor=white)
![Pi-hole](https://img.shields.io/badge/Pi--hole-96060C?style=flat-square&logo=pi-hole&logoColor=white)
![WireGuard](https://img.shields.io/badge/WireGuard-88171A?style=flat-square&logo=wireguard&logoColor=white)
![Nextcloud](https://img.shields.io/badge/Nextcloud-0082C9?style=flat-square&logo=nextcloud&logoColor=white)
![Jellyfin](https://img.shields.io/badge/Jellyfin-00A4DC?style=flat-square&logo=jellyfin&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu_Server-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Apache](https://img.shields.io/badge/Apache-F28C28?style=flat-square&logo=apache&logoColor=white)
<br>
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi_4-A22846?style=flat-square&logo=raspberry-pi&logoColor=white)
![Orange Pi](https://img.shields.io/badge/Orange_Pi-FF7F00?style=flat-square)
<br>

</div>

## ✨ What is this?

A small self-hosted homelab built around a Raspberry Pi 5 and an Orange Pi 3B. The Raspberry Pi 5 runs Home Assistant OS, providing the main home automation platform, while the Orange Pi 3B runs Ubuntu Server and hosts several services through Docker. Mosquitto provides MQTT communication, with a custom MQTT script used to monitor and control the Orange Pi 3B fans. Pi-hole handles DNS filtering for the local network, while WireGuard provides secure remote VPN access. Docker services include Nextcloud, Jellyfin, MariaDB, Redis and Portainer. The setup also includes ESPHome devices and smart power devices integrated with Home Assistant. A UPS (Uninterruptible Power Supply) protects the Raspberry Pi 5 and router from power outages, helping keep the core network and home automation infrastructure online during short power interruptions.

## 🧱 The stack
### Raspberry Pi 5

- **Home Assistant OS**

- Home automation, networking and device management.

| Service | Role |
| :--- | :--- |
| **Home Assistant** | Automation & state engine |
| **Mosquitto** | MQTT broker |
| **ESPHome** | ESP device integration |
| **Pi-hole** | Network-wide DNS filtering |
| **WireGuard** | VPN & remote access |

- `8 GB RAM` · `512 GB SSD`

---

### Orange Pi 3B

- **Ubuntu Server**

- Secondary server for fan control and containerized services.

| Service | Role |
| :--- | :--- |
| **Fan Control** | MQTT-based fan control script |
| **Portainer** | Docker container management |
| **Nextcloud** | Self-hosted files, calendar & contacts |
| **Jellyfin** | Self-hosted media server |
| **MariaDB** | Database |
| **Redis** | Cache & data store |

- `8 GB RAM` · `512 GB SSD`

---

### Infrastructure

- **Raspberry Pi** → **Home Assistant** ↔ **Mosquitto** ↔ **Orange PI** ↔ **Fan Control**

- **OrangePI** → **Docker** → Nextcloud · Jellyfin · MariaDB · Redis · Portainer

- **Raspberry Pi** → **Home Assistant** → **WireGuard** → Remote access

- **Raspberry Pi** → **Home Assistant** ↔ **Pi-hole** → Network-wide DNS filtering

## 🗺️ How it connects

<div align="center">

<img src="img/map.svg" alt="Home Lab network diagram" width="900">

</div>

## 💡 Devices

| | Device | Location | Link | Role |
|:-:|:--|:--|:--|:--|
| 💡 | Double Smart Switch | Bedroom Lights | Tuya Wifi | On/Off |
| 💡 | Smart Leds | Bedroom, table lamp | Tuya/Wifi | On/Off, RGBW |
| 🔌 | Smart Plug | Additional Power | Tuya/Wifi | On/Off |
| 🔌 | Smart Power Strip | Desktop Power | Tuya/Wifi | On/Off |
| 🖥️ | Desktop PC  | Bedroom wall | MQTT | On/Off, Commands |

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
