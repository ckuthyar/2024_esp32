import umail
import network
import machine
import utime

rtc = machine.RTC()
rtc.datetime((2024, 1, 18, 4, 14, 10, 0, 0)) # (year, month, day, weekday, hour, minute, second, subsecond)

ssid = 'vivo Y100A'
password = 'personal.s'

sender_email = ''
sender_name = 'ESP32'
sender_password = ''
recipient_email = []
email_subject = 'BaatCheet English'

def connect_wifi(ssid, password):
   
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while not station.isconnected():
        pass
    print('Connection successful')
    print(station.ifconfig())
   
position=0

connect_wifi(ssid, password)
h1=["14","15","16"]
m1=["0","4","8","12","16","20","24","28","32","36","40","44","48","52","56","60"]
m2=["2","6","10","14","18","22","26","30","34","38","42","46","50","54","58","0"]
while True:
    year, month, day, weekday, hour, minute, second, subsecond = rtc.datetime()
    hour = "{:02d}".format(hour)
    minut = "{:02d}".format(minute)
    for i in range(0,len(h1),1):
        for j in range(0,len(m1),1):
            if hour == h1[i]:
                if minut == m1[j] or minut ==m2[j]:
                    for i in range(0,len(recipient_email),1):
                        smtp = umail.SMTP('smtp.mailgun.org', 465, ssl=True)
                        smtp.login(sender_email, sender_password)
                        smtp.to(recipient_email[i])
                        mes1= "nbhjklvbnm"
                        smtp.write("Subject:" + email_subject + "\n")
                        email_body=mes1
                        smtp.write(email_body)
                        smtp.send()
                        position=(position+1)%size
                        smtp.quit()
                        print("yes")
    utime.sleep(60)