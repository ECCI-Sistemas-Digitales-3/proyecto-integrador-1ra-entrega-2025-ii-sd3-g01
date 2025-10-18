from umqtt.simple import MQTTClient
import network
from machine import Pin
import time
import machine   

# ==========================
# CONFIGURACIONES GENERALES
# ==========================
SSID = "TIGO-E325"          
PASSWORD = "7989956371"
BROKER = "192.168.1.9"  
CLIENT_ID = "ESP32_BOMBA"
TOPIC_CONTROL = b"bomba/control"
TOPIC_ESTADO = b"bomba/estado"

# Pines
led = Pin(2, Pin.OUT)        # LED integrado (indicador)
bomba = Pin(32, Pin.OUT)      # Pin de control del relé/bomba

# ==========================
# CONEXIÓN WiFi
# ==========================
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando a WiFi...")
        wlan.connect(SSID, PASSWORD)
        t = 0
        while not wlan.isconnected() and t < 15:
            time.sleep(1)
            print(".", end="")
            t += 1
    if wlan.isconnected():
        print("\n✅ Conectado a WiFi:", wlan.ifconfig())
    else:
        print("\n❌ No se pudo conectar a WiFi")
        machine.reset()

# ==========================
# FUNCIÓN DE CALLBACK MQTT
# ==========================
def mensaje_mqtt(topic, msg):
    print("📩 Mensaje recibido:", topic, msg)
    if msg == b"ON":
        led.value(1)
        bomba.value(1)
        print("💧 Bomba ENCENDIDA")
        client.publish(TOPIC_ESTADO, b"ENCENDIDA")
    elif msg == b"OFF":
        led.value(0)
        bomba.value(0)
        print("🛑 Bomba APAGADA")
        client.publish(TOPIC_ESTADO, b"APAGADA")

# ==========================
# CONEXIÓN MQTT
# ==========================
def conectar_mqtt():
    global client
    client = MQTTClient(CLIENT_ID, BROKER)
    client.set_callback(mensaje_mqtt)
    client.connect()
    print("📡 Conectado al broker MQTT:", BROKER)
    client.subscribe(TOPIC_CONTROL)
    print("🔔 Suscrito al tema:", TOPIC_CONTROL)

# ==========================
# PROGRAMA PRINCIPAL
# ==========================
try:
    conectar_wifi()
    conectar_mqtt()
    client.publish(TOPIC_ESTADO, b"APAGADA")  # Estado inicial
    while True:
        client.check_msg()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("🛑 Programa detenido manualmente")
    client.disconnect()
except Exception as e:
    print("⚠️ Error:", e)
    machine.reset()
