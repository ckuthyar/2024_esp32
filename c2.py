import network

ssid = ''
password = ''

def connect_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    if not station.isconnected():
        station.active(True)
        station.connect(ssid, password)
        print("......")
        while not sta_if.isconnected():
            pass
    print('Connection successful')
    print(station.ifconfig())
connect_wifi(ssid,password)