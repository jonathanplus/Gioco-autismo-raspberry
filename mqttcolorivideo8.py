# import
import time
from time import sleep
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import subprocess

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
GPIO.output(ventolaPin,GPIO.HIGH)

# broker IP address
Broker = "ip broker"

# topics (reverse Client A topics)
pub_topic = "topic publisch"
sub_topic = "topic subscrive"

# on connect function
def on_connect(client, userdata, flags, rc):
    print("Client che riceve comandi attivato con codice: " + str(rc))
    client.subscribe(sub_topic)
# 000 = rosso/100 = verde/110 = blu/111 = giallo/011 = bianco/001 = viola/ 010 = arcobaleno.
# on message function
def on_message(client, userdata, message):
    message = str(message.payload.decode("utf-8"))
    print("Comando ricevuto: " + message)
    if message == "rosso" :
        moviepath = 'video/colori/rosso.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #sequenza pin per selezionare spettacolo su striscia led.
        GPIO.output(selPin,GPIO.HIGH) 
        time.sleep (5)
        GPIO.output(selPin,GPIO.LOW)
		
		
    elif message == "verde" :
        moviepath = 'video/colori/verde.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350',  moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #sequenza pin per selezionare spettacolo su striscia led.
        GPIO.output(bn1Pin,GPIO.HIGH)
        time.sleep (2)
        GPIO.output(selPin,GPIO.HIGH)
        time.sleep (5)
        GPIO.output(selPin,GPIO.LOW)
        GPIO.output(bn1Pin,GPIO.LOW)
		
		
    elif message == "blu" :
        moviepath = 'video/colori/blu.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #sequenza pin per selezionare spettacolo su striscia led.
        GPIO.output(bn1Pin,GPIO.HIGH)
        GPIO.output(bn2Pin,GPIO.HIGH)
        time.sleep (2)
        GPIO.output(selPin,GPIO.HIGH)
        time.sleep (5)
        GPIO.output(selPin,GPIO.LOW)
        GPIO.output(bn1Pin,GPIO.LOW)
        GPIO.output(bn2Pin,GPIO.LOW)
        
    elif message == "giallo" :
        moviepath = 'video/colori/giallo.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #sequenza pin per selezionare spettacolo su striscia led.
        GPIO.output(bn1Pin,GPIO.HIGH)
        GPIO.output(bn2Pin,GPIO.HIGH)
        GPIO.output(bn3Pin,GPIO.HIGH)
        time.sleep (2)
        GPIO.output(selPin,GPIO.HIGH)
        time.sleep (5)
        GPIO.output(selPin,GPIO.LOW)
        GPIO.output(bn1Pin,GPIO.LOW)
        GPIO.output(bn2Pin,GPIO.LOW)
        GPIO.output(bn3Pin,GPIO.LOW)
		
    elif message == "bianco" :
        moviepath = 'video/colori/bianco.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350',  moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
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

    elif message == "viola" :
        moviepath = 'video/colori/viola.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350',  moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #sequenza pin per selezionare spettacolo su striscia led.
        GPIO.output(bn3Pin,GPIO.HIGH)
        time.sleep (2)
        GPIO.output(selPin,GPIO.HIGH)
        time.sleep (5)
        GPIO.output(selPin,GPIO.LOW)
        GPIO.output(bn3Pin,GPIO.LOW)

    elif message == "arcobaleno" :
        moviepath = 'video/colori/arcobaleno.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #sequenza pin per selezionare spettacolo su striscia led.
        GPIO.output(bn2Pin,GPIO.HIGH)
        time.sleep (2)
        GPIO.output(selPin,GPIO.HIGH)
        time.sleep (5)
        GPIO.output(selPin,GPIO.LOW)
        GPIO.output(bn2Pin,GPIO.LOW)
    
    if message == "ventola" :
        moviepath = 'video/colori/ventola.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
        #accensione rele ventola 10 secondi
        GPIO.output(ventolaPin,GPIO.LOW)
        time.sleep (10)
        GPIO.output(ventolaPin,GPIO.HIGH)	

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
