import gen_test
import base64
from  play_video import *

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = 'class.iottalk.tw' # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'Music_to_Video'
IDF_list = ['MP4_I']
ODF_list = ['Sentence_O', 'MP4_O']
device_id = '31283301712230428 ' #if None, device_id = MAC address
device_name = 'eden_device'
exec_interval = 10  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

have_recieved = [0]

def MP4_I():
    if have_recieved[0] == 0: return None
    have_recieved[0] = 0
    mp4_file = open(gen_test.filename, 'rb')
    mp4_binary_data = mp4_file.read()
    base64_encoded = base64.b64encode(mp4_binary_data)
    base64_string = base64_encoded.decode('utf-8')
    return base64_string

def MP4_O(data:list):
    print("len of data) =",len(data[0])) 
    if len(data[0]) > 0:
        play_video(data[0])
    else:
        print("error")


def Sentence_O(data:list):
    have_recieved[0] = 1
    gen_test.gen_video(data)
