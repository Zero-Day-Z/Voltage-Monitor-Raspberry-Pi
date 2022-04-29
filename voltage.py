import time
from ADCDevice import *
import smtplib

adc = ADCDevice()

#Email Notification
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = '#email
GMAIL_PASSWORD = #password

class Emailer:
    def sendmail(self, recipient,  subject, content):
        #Creating the headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
            "To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

def setup():
  global adc
  if(adc.detectI2C(0x48)):
    adc = PCF8591()
  elif(adc.detectI2C(0x4b)):
    adc = ADS7830()
  else:
    print("Correct I2C address not found")
    exit(-1)
def loop():
  while True:
    value = adc.analogRead(0)
    voltage = value / 255.0 * 3.3
    print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
    time.sleep(1)
    if voltage > 2.0:
        print("high voltage detected!")
        sender = Emailer()
        sendTo = #recippient email
        emailSubject = "IOT Research: Voltage"
        emailContent = "This is the Pi in the lab.\n High Voltage Detected! \n Measurements:\n ADC Value: " +str(value) +"\nVoltage: "+str(voltage)
        sender.sendmail(sendTo, emailSubject, emailContent)

def destroy():
  adc.close()
  
if __name__ == '__main__': 
  print ('Program is starting ... ')
  try:
    setup()
    loop()
  except KeyboardInterrupt:
    destroy()
