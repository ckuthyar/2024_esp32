import umail
import network

# Your network credentials
ssid = 'BSNL_rtd'
password = ''

# Email details
sender_email = 'postmaster@sandbox1b5fbfb0fd9c4dcda06a9344c83c89c3.mailgun.org'
sender_name = 'ESP32'
sender_password = ''
recipient_email = 'ckuthyar@gmail.com'
email_subject = 'Testing at 2024-714_2118'
email_body = 'From cS'

def connect_wifi(ssid, password):
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())
    
# Connect to your network
connect_wifi(ssid, password)
smtp = umail.SMTP('smtp.mailgun.org', 465, ssl=True)
smtp.login(sender_email, sender_password)
smtp.to(recipient_email)
smtp.write("Subject:" + email_subject + "\n")
smtp.write(email_body)
smtp.send()
smtp.quit()

print("Email sent!")

