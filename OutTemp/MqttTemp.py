import paho.mqtt.client as paho
import time


class MqttTemp(object):

    def __init__(self, topic):
        print "Init Subscribe..."
        self._client = paho.Client()
        self._client.on_subscribe = self.on_subscribe
        self._client.on_message = self.on_message
        self._client.connect("sundback.ddns.net", 1883)
        self._client.subscribe(topic , qos=1)
        self._client.loop_start()
        self._lastvalue = "-"

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_message(self,client, userdata, msg):
        self._lastvalue = msg.payload
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    def read(self):
        if self._lastvalue == "-":
            test = "  " + self._lastvalue
        else:
            test = str(int(round(float(self._lastvalue),0)))

        test = test + 'g'

        if len(test) == 1:
            test = '   ' + test
        else:
            if len(test) == 2:
                test = '  ' + test
            else:
                if len(test) == 3:
                    test = ' ' + test
        return test

if __name__ == "__main__":
    sub=MqttTemp("ev39/temp")

    while True:
        print sub.read()
        time.sleep(2)
