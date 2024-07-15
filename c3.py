import network
from umail import SMTP
import umail

# Wi-Fi settings
ssid = "BSNL_rtd"
password = ""

# Mailgun settings
sender_email = 'postmaster@sandbox1b5fbfb0fd9c4dcda06a9344c83c89c3.mailgun.org'
sender_name = 'ESP32'
sender_password = ''
recipient_email = 'ckuthyar@gmail.com'
email_subject = 'Testing at 2024-714_2118'
email_body = 'From cS'
# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    pass

# Send email
smtp = umail.SMTP('smtp.mailgun.org', 465, ssl=True)
smtp.login(sender_email, sender_password)
smtp.to(recipient_email)
smtp.write("Subject:" + email_subject + "\n")
smtp.write(email_body)
smtp.send()
smtp.quit()

print("Email sent!")

