from paho.mqtt import client as mqtt_client
from http import client
import pymongo
import json

client = pymongo.MongoClient('mongodb+srv://adel-khouly:adel-khouly9499@clusterofmongoprogect.xy8ec.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
print(client.list_database_names())

db=client['mongoProject']

print(db.list_collection_names())

collection=db.randomData



mqttBroker = 'broker.emqx.io'
port = 1883
topic = "/python/mqtt/adel"
#client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client("Python Code")
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(mqttBroker, port)
    return client

def subscribe(client: mqtt_client):
    # def on_message(client, userdata, msg):
    #     print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    #     print(msg.payload.decode())
    
    def on_message(client, userdate, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        randomDataDocument =  json.loads(f"{msg.payload.decode()}")
        data1= db.randomData.insert_one(randomDataDocument).inserted_id
        print(data1)
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()



