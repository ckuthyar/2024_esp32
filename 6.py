import network
import urequests
import ujson

ssid = "vivo Y100A"
password = ""

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass

    print('Network connected:', wlan.ifconfig())

def post_request(url, data):
    headers = {'Content-Type': 'application/json'}
    response = urequests.post(url, data=ujson.dumps(data), headers=headers)
    return response

def get_responce(url):
    return urequests.get(url)
connect_to_wifi(ssid, password)

url = 'https://eobsfgwtm05ze9m.m.pipedream.net'
data = {
    'test':'event1'
}

#response = post_request(url, data)
responce=get_responce(url)
print('Response:', responce.text)
print(ujson.loads(responce.text))


responce.close()
