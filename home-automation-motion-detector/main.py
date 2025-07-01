import machine
import time
import network
import urequests

ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected():
    pass

print('Connected to Wi-Fi')

pir = machine.Pin(14, machine.Pin.IN)

def send_notification():
    url = 'http://your-server-or-api-endpoint'
    try:
        response = urequests.get(url + '?motion=detected')
        response.close()
    except:
        print("Failed to send notification")

while True:
    if pir.value() == 1:
        print("Motion Detected!")
        send_notification()
        time.sleep(10)
    time.sleep(1)
