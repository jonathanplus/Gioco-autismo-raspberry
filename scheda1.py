### Client B ###

# import
import time
from time import sleep
import paho.mqtt.client as mqtt
import subprocess
import RPi.GPIO as GPIO 

# pulsante
pulsantePin = 4

# setup gpio
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pulsantePin, GPIO.IN)



# broker IP address
Broker = "ip broker"

# topics (reverse Client A topics)
pub_topic = "topic pubblish"
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
        moviepath = 'video/videotommy/Whiskey.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep (1)
        print ("parte il ciclo")
        #a = 34 secondi per intervenire sul pulsante se si vuole interrompere il video e far tornare il telecomando on
        a = 0
        #b = pubblica x per far tornare il telecomando on
        b = 0
        while a <= 169:
            print ("entrato nel ciclo")
            input=GPIO.input(pulsantePin);
            if(input == 0):
                time.sleep (.2)
                a = a + 1 
                print (a)
            else:
                print ("spento il video")
                omxprocess.stdin.write(b'q')
                a = 170
                b = 1
        if b == 0 :
            print ("video finito")
            client.publish(pub_topic, "a")
            print ("a")
        else :
            client.publish(pub_topic, "x")
            print ("x")

    elif message == "Button2 pressed!" :
        print ("lancia il video")
        moviepath = 'video/videotommy/Cinque_Scimmiette.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep (1)
        print ("parte il ciclo")
        #a = 34 secondi per intervenire sul pulsante se si vuole interrompere il video e far tornare il telecomando on
        a = 0
        #b = pubblica x per far tornare il telecomando on
        b = 0
        while a <= 169:
            print ("entrato nel ciclo")
            input=GPIO.input(pulsantePin);
            if(input == 0):
                time.sleep (.2)
                a = a + 1
                print (a)
            else:
                print ("spento il video")
                omxprocess.stdin.write(b'q')
                a = 170
                b = 1
        if b == 0 :
            print ("video finito")
            client.publish(pub_topic, "b")
            print ("b")
        else : 
            client.publish(pub_topic, "x")
            print ("x")


    elif message == "Button3 pressed!" :
        print ("lancia il video")
        moviepath = 'video/videotommy/La_macchina.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep (1)
        print ("parte il ciclo")
        #a = 34 secondi per intervenire sul pulsante se si vuole interrompere il video e far tornare il telecomando on
        a = 0
        #b = pubblica x per far tornare il telecomando on
        b = 0
        while a <= 169:
            print ("entrato nel ciclo")
            input=GPIO.input(pulsantePin);
            if(input == 0):
                time.sleep (.2)
                a = a + 1
                print (a)
            else:
                print ("spento il video")
                omxprocess.stdin.write(b'q')
                a = 170
                b = 1
        if b == 0 :
            print ("video finito")
            client.publish(pub_topic, "c")
            print ("c")
        else :
            client.publish(pub_topic, "x")
            print ("x")
    elif message == "Button4 pressed!" :
        print ("lancia il video")
        moviepath = 'video/videotommy/fattoria.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep (1)
        print ("parte il ciclo")
        #a = 34 secondi per intervenire sul pulsante se si vuole interrompere il video e far tornare il telecomando on
        a = 0
        #b = pubblica x per far tornare il telecomando on
        b = 0
        while a <= 169:
            print ("entrato nel ciclo")
            input=GPIO.input(pulsantePin);
            if(input == 0):
                time.sleep (.2)
                a = a + 1
                print (a)
            else:
                print ("spento il video")
                omxprocess.stdin.write(b'q')
                a = 170
                b = 1
        if b == 0 :
            print ("video finito")
            client.publish(pub_topic, "d")
            print ("d")
        else :
            client.publish(pub_topic, "x")
            print ("x")




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
