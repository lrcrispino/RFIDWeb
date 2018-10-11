
import paho.mqtt.client as mqttClient
import time
import random
from django.utils import timezone

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        global tries
        tries += 1
        print("xConnected to broker"+str(tries)+"rc"+str(rc))
        global Connected                
        Connected = True 
        client.subscribe("scans")
        client.subscribe("status")
    else:
        print("Connection failed") 

def on_message(client, userdata, message):
    #global rawdata
    from app.models import rawdata
    from app.models import accesslog
    from app.models import userlist
    from app.models import scanners
    datas = rawdata.objects.get(pk=1)
    payload = str(message.payload.decode("utf-8"))
    print("Message received: ", payload)
    datas.text += str(timezone.localtime(timezone.now()))[0:19]
    datas.text += " : "
    datas.text += payload
    datas.text += "\n"
    datas.save()
    if message.topic == "scans":
        payload2 = payload.split(",")
        try:
            payload2[1]
        except IndexError:
            None
        else:
            try:
                scanneduser = userlist.objects.get(scan_id = payload2[1])
                
            except:
                scanneduser = userlist.objects.get(scan_id = "0")
            try:
                scanner = scanners.objects.get(clientid = payload2[0])
            except:
                pass
            new_entry = accesslog(
                entrydate = timezone.now(),
                username = scanneduser, 
                scan_id = payload2[1], 
                area = scanner.area+" "+scanner.door, 
                scan_type = scanner.direction,
                action = check_action(client,scanneduser,scanner))
            new_entry.save()
    elif message.topic == "status":
        try:
            found = scanners.objects.get(clientid = payload)
            found.online = True
            found.save()
        except:
            pass
        

        

def check_action(client,scanneduser, scanner):
    if scanner.direction == 'in':
        #check already inside, check auth, open door, add to list
        if not check_inside(scanneduser, scanner.area):
            if check_auth(scanneduser, scanner.area):
                scanneduser.status = "in"
                scanneduser.area = scanner.area
                scanneduser.save()
                client.publish("doors",scanner.clientid)
                return "Entering"
            else:
                return "Unauthorized"
        else:
            scanneduser.area = scanner.area
            scanneduser.save()
            client.publish("doors",scanner.clientid)
            return "Already Inside"
    elif scanner.direction == "out":
        #check already outside, remove from list (open door?)
        if check_inside(scanneduser, scanner.area):
            scanneduser.status = "out"
            scanneduser.area = scanner.area
            scanneduser.save()
            return "Leaving"
        else:
            scanneduser.area = scanner.area
            scanneduser.save()
            return "Already Outside"
    else:
        return "Invalid Scan Type"

def check_inside(scanneduser, scan_area):
    #from app.models import userlist
    if scanneduser.status == "in":
        return True
    else:
        return False

def check_auth(scanneduser, scan_area):
    if  scanneduser.scan_id == "0":
        return False
    else:
        return True

def pingscanners():
    global client
    client.publish("doors","?")

def _init():
    payload = ""
    global Connected
    Connected = False  
    global tries
    tries = 0
    broker_address= "quack.hopto.org"  
    port = 1883 
    global client
    client = mqttClient.Client("WebServer")    
    client.username_pw_set("RFID","pineapple")
    client.on_connect= on_connect                  
    client.on_message= on_message                 
    try:
        client.connect(broker_address, port=port)
    except:
        broker_address= "localhost"
        client.connect(broker_address, port=port)
        print("Switched to localhost")
    client.loop_start()
    while Connected != True:    
        time.sleep(0.1)


#client.loop_start()



#try:
#	while True:
#		window.mainloop()
#except KeyboardInterrupt:
#	print("disconnecting")
#	client.disconnect()
#	print("disconnected")
#	client.loop_stop()
#	print("loop stopped")