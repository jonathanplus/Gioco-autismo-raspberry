### Client B ###

# import
import time
from time import sleep
import paho.mqtt.client as mqtt
import subprocess
import RPi.GPIO as GPIO 

# LED pins
selPin = 26
bn1Pin = 5
bn2Pin = 6
bn3Pin = 13
ventolaPin = 19

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(selPin, GPIO.OUT)
GPIO.setup(bn1Pin, GPIO.OUT)
GPIO.setup(bn2Pin, GPIO.OUT)
GPIO.setup(bn3Pin, GPIO.OUT)
GPIO.setup(ventolaPin, GPIO.OUT)
GPIO.output(ventolaPin, GPIO.HIGH)



# broker IP address
Broker = "ip broker"

# topics (reverse Client A topics)
pub_topic = "topic publish"
sub_topic = "topic subscrive"

# on connect function
def on_connect(client, userdata, flags, rc):
    print("Client che riceve comandi attivato con codice: " + str(rc))
    client.subscribe(sub_topic)

# on message function
def on_message(client, userdata, message):
    message = str(message.payload.decode("utf-8"))
    print("Comando ricevuto: " + message)
    if message == "Button pressed!" :
        print ("lancia il video")
        moviepath = 'video/colori/arcobaleno.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #sequenza pin per selezionare spettacolo su striscia led.
        GPIO.output(bn2Pin,GPIO.HIGH)
        time.sleep (2)
        GPIO.output(selPin,GPIO.HIGH)
        time.sleep (5)
        GPIO.output(selPin,GPIO.LOW)
        GPIO.output(bn2Pin,GPIO.LOW)

        print ("video finito")
        client.publish(pub_topic, "t")
        print ("t")

    elif message == "Button2 pressed!" :
        print ("lancia il video")
        moviepath = 'video/colori/ventola.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #accensione rele ventola 10 secondi
        print ("video finito")
        GPIO.output(ventolaPin,GPIO.LOW)
        print ("gpio low 10 sec")
        time.sleep (10)
        GPIO.output(ventolaPin,GPIO.HIGH)	
        print ("video finito")
        client.publish(pub_topic, "u")
        print ("u")


    elif message == "Button3 pressed!" :
        print ("lancia il video")
        moviepath = 'video/colori/bianco.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #sequenza pin per selezionare spettacolo su striscia led.
        GPIO.output(bn2Pin,GPIO.HIGH)
        GPIO.output(bn3Pin,GPIO.HIGH)
        time.sleep (2)
        GPIO.output(selPin,GPIO.HIGH)
        time.sleep (5)
        GPIO.output(selPin,GPIO.LOW)
        GPIO.output(bn2Pin,GPIO.LOW)
        GPIO.output(bn3Pin,GPIO.LOW)
        print ("video finito")
        client.publish(pub_topic, "v")
        print ("v")
    elif message == "Button4 pressed!" :
        print ("lancia il video")
        moviepath = 'video/colori/viola.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #sequenza pin per selezionare spettacolo su striscia led.
        GPIO.output(bn3Pin,GPIO.HIGH)
        time.sleep (2)
        GPIO.output(selPin,GPIO.HIGH)
        time.sleep (5)
        GPIO.output(selPin,GPIO.LOW)
        GPIO.output(bn3Pin,GPIO.LOW)
        print ("video finito")
        client.publish(pub_topic, "z")
        print ("z")




# on publish function
def on_publish(mosq, obj, mid):
    print("Risposta inviata con message id: " + str(mid))

# instantiate paho MQTT client
client = mqtt.Client()
client.username_pw_set(username="nome broker",password="password")
# add on_connect and on_message functions to client events
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

# connect paho client to mosquitto broker (IP, port, timeout)
client.connect(Broker, 1883, 60)

# client loops forever
client.loop_forever()
