import paho.mqtt.client as mqtt
import os
import time
import threading
import psutil

gpios = {
    "gpio119": 119,
    "gpio129": 129
}

def find_hwmon_path(device_name):
    hwmon_base = "/sys/class/hwmon"
    try:
        for hwmon in sorted(os.listdir(hwmon_base)):
            name_path = os.path.join(hwmon_base, hwmon, "name")
            if os.path.exists(name_path):
                with open(name_path, "r") as f:
                    if f.read().strip() == device_name:
                        return os.path.join(hwmon_base, hwmon)
    except Exception as e:
        print(f"[ERROR] Buscando hwmon '{device_name}': {e}")
    return None

def export_gpio(gpio):
    gpio_path = f"/sys/class/gpio/gpio{gpio}"
    if not os.path.exists(gpio_path):
        try:
            with open("/sys/class/gpio/export", "w") as f:
                f.write(str(gpio))
        except PermissionError:
            print(f"[ERROR] Permiso denegado al exportar GPIO {gpio}. Ejecuta como root.")
            return False
    try:
        with open(f"{gpio_path}/direction", "w") as f:
            f.write("out")
    except:
        pass
    return True

def write_gpio(gpio, value):
    gpio_path = f"/sys/class/gpio/gpio{gpio}/value"
    try:
        with open(gpio_path, "w") as f:
            f.write("1" if value else "0")
    except PermissionError:
        print(f"[ERROR] Permiso denegado al escribir en GPIO {gpio}. Ejecuta como root.")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT")
        client.subscribe("orangepi/gpio/#")
        client.subscribe("orangepi/reboot")
        client.publish("orangepi/status", "Online", retain=True)
        for name, pin in gpios.items():
            if export_gpio(pin):
                write_gpio(pin, True)
        threading.Thread(target=publicar_datos, daemon=True).start()
    else:
        print(f"Error de conexión, código: {rc}")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode().lower()
    pin_name = topic.split("/")[-1]
    if pin_name in gpios:
        gpio = gpios[pin_name]
        if export_gpio(gpio):
            write_gpio(gpio, payload == "on")
    if topic == "orangepi/reboot" and payload in ("on", "1", "true"):
        print("Reboot solicitado vía MQTT...")
        os.system("reboot")

def obtener_uptime():
    try:
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
        days = int(uptime_seconds // 86400)
        hours = int((uptime_seconds % 86400) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        return f"{days}d {hours}h {minutes}m"
    except:
        return None

def publicar_datos():
    hwmon_cpu  = find_hwmon_path("cpu_thermal")
    hwmon_nvme = find_hwmon_path("nvme")

    while True:
        try:
            if hwmon_cpu:
                with open(f"{hwmon_cpu}/temp1_input") as f:
                    temp_c = int(f.read().strip()) / 1000.0
                client.publish("orangepi/temperature", f"{temp_c:.2f}", retain=True)

            if hwmon_nvme:
                with open(f"{hwmon_nvme}/temp1_input") as f:
                    temp_c = int(f.read().strip()) / 1000.0
                client.publish("orangepi/temperature_nvme", f"{temp_c:.2f}", retain=True)

            cpu_percent = round(psutil.cpu_percent(interval=1), 1)
            client.publish("orangepi/cpu_percent", cpu_percent, retain=True)

            mem_percent = round(psutil.virtual_memory().percent, 1)
            client.publish("orangepi/memory_percent", mem_percent, retain=True)

            disk_used_gb = round(psutil.disk_usage("/").used / (1024 ** 3), 2)
            client.publish("orangepi/disk_used_gb", disk_used_gb, retain=True)

            uptime_str = obtener_uptime()
            if uptime_str:
                client.publish("orangepi/uptime", uptime_str, retain=True)

        except Exception as e:
            print(f"[ERROR] Publicación: {e}")
            hwmon_cpu  = find_hwmon_path("cpu_thermal")
            hwmon_nvme = find_hwmon_path("nvme")

        time.sleep(5)

client = mqtt.Client()
client.will_set("orangepi/status", "Offline", retain=True)
client.username_pw_set("YOUR-MQTT-USER", "YOUR-MQTT-PASS")
client.on_connect = on_connect
client.on_message = on_message
client.connect("YOUR-IP", 1883, 60)
client.loop_forever()
