import network
from umail import SMTP
import umail

# Wi-Fi settings
ssid = "vivo Y100A"
password = "personal.s"

# Mailgun settings
sender_email = 'postmaster@sandbox1b5fbfb0fd9c4dcda06a9344c83c89c3.mailgun.org'
sender_name = 'ESP32'
sender_password = '11092168d0803e4fbb3747c0ded624a6-4c955d28-e55ef157'
recipient_email = 'ssvision064@gmail.com'
email_subject = 'BaatCheet English'
email_body = 'sakmkasas'
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
