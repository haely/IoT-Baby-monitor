# Contributors:
# Haely Shah
# Josiah Morrison


# Importing the nexmo library URL: https://developer.nexmo.com 
import nexmo  
import RPi.GPIO as GPIO
from time import sleep

sensor_pin = 17. # Initialized GPIO 17 for motion sensor

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)         # Declared GPIO 17 as input pin

# Connecting to the nexmo using API key and API secret
client = nexmo.Client(key='ad927137', secret='SrZcNbtH3xEEZMro')

receiver = '+4082813385' # The number at which you want to send to - no country code required for US cellphones, Ryan's google cell
message = '''Warning'''

# Function to send message
def send_sms():
    # Sending the message
    response = client.send_message({'from' : 'Nexmo', 'to' : receiver, 'text' : message})
    # Getting a response message
    response = response['messages'][0]
    
    # Checking whether we are successful or if we got an error
    if response['status'] == '0':
        print 'send message', response['message-id']
    else:
        print 'Error:' , response['error']

while True:
    try:
        # Reading the motion sensor pin state
        pin_state = GPIO.input(sensor_pin)
        if pin_state==0:                 # When output from motion sensor is LOW
            print "Body Sound Not Detected",pin_state
            sleep(0.1)
            
        elif pin_state==1:               # When output from motion sensor is HIGH
            print "Body Sound Detected",pin_state
            send_sms()
            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleaup()
