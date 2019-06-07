import paho.mqtt.client as mqtt
import subprocess
import time

Broker = "ip broker"
pub_topic = "topic pubblish"
sub_topic = "topic subscrive"

def on_connect(client, userdata, flags, rc):
    print("Client che riceve comandi attivato con codice: " + str(rc))
    client.subscribe(sub_topic)

def on_message(client, userdata, message):
    message = str(message.payload.decode("utf-8"))
    print("Comando ricevuto: " + message)
    if message == "dario" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/dario.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message ==  "mamma":
        print ("lancia il video")
        moviepath = 'video/fotoriky/mamma_l.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "anna" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/n_anna.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "cosimo" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/cosimo.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "carmelo" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/carmelo.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "basta" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/basta.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "piange" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/pianto.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "felice" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/felice.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "lele" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/lele.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "mare" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/mare.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "nanna" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/nanna.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "palla" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/palla.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "papa1" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/papa3.mp4'
        omxprocess = subprocess.Popen(['omxplayer', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "riki" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/riky.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "silenzio" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/silenzio.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "tommy" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/tommy.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "simone" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/simone.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "nono" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/nono.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(14)
        omxprocess.stdin.write(b'q')
    elif message == "ancora" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/ancora.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "milo" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/zio_milo.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "mariagrazia" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/zia_m_r_g.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "vittorio" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/c_vittorio.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "pappa" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/pappa.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(16)
        omxprocess.stdin.write(b'q')
    elif message == "emilio" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/emilio.mp4'
        omxprocess = subprocess.Popen(['omxplayer' , moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')
    elif message == "luca" :
        print ("lancia il video")
        moviepath = 'video/fotoriky/luca.mp4'
        omxprocess = subprocess.Popen(['omxplayer', '--vol', '350', moviepath],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        time.sleep(10)
        omxprocess.stdin.write(b'q')



def on_publish(mosq, obj, mid):
    print("Risposta inviata con message id: " + str(mid))

# instantiate paho MQTT client
client = mqtt.Client()
client.username_pw_set(username="nome broker",password="pasword")
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect(Broker, 1883, 60)

client.loop_forever()

