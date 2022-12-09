
import sys
import time
from pyskyqremote.skyq_remote import SkyQRemote                     #Main class
from pyskyqremote.classes.device import device_decoder              #Class to decode device json responses
from pyskyqremote.classes.media import media_decoder                #Class to decode medeia json responses

#All Dependencies should be copied to local /user folder.
#The Depency list is:
#    anyio==3.6.2
#asks==3.0.0
#async-generator==1.10
#attrs==22.1.0
#certifi==2022.9.24
#cffi==1.15.1
#charset-normalizer==2.1.1
#debugpy==1.6.4
#exceptiongroup==1.0.4
#h11==0.14.0
#idna==3.4
#module-name==0.5.1
#multidict==6.0.3
#outcome==1.2.0
#pip==21.2.3
#pycparser==2.21
#pyskyq==0.6.1
#pyskyqremote==0.3.21
#python-dateutil==2.8.2
#requests==2.28.1
#setuptools==57.4.0
#six==1.16.0
#sniffio==1.3.0
#sortedcontainers==2.4.0
#trio==0.22.0
#trio-websocket==0.9.2
#urllib3==1.26.13
#websocket-client==1.4.2
#wsproto==1.2.0
#xmltodict==0.13.0
#yarl==1.8.2


def data_received_callback(json):
    print("PYTHON: Printing from simpltest.py subscribe() callback: " + json)

def crestron_main(module_info_object):
    print("PYTHON: reached crestron_main")
    print("PYTHON: " + repr(module_info_object))

    my_guid = module_info_object.uid
    args = module_info_object.args
    
    
    print("PYTHON: guid = " + repr(my_guid) + " args = " + repr(args))
    
    module_info_object.subscribe(data_received_callback)

    cmd = args[0]


    if cmd == "connect":
        print("Executing Connect Command at ip: " + args[1])
        self.client = SkyQRemote(args[1])
        check_device_connection()
    else:
        try:
            client.press(cmd)
            print("PYTHON: " + cmd + "executed")
            refresh_fb()
        except Exception as e:
            print("Python: Failed to execute " + cmd )
    


def main():
    print("PYTHON: Hello from simpltest.py")
    print("PYTHON: Argument list: " + str(sys.argv))
    
def check_device_connection():
      device = self.client.get_device_information()
      if device is not None:
          module_info_object.set("connection_fb_1")         #set Connection_FB 1
      else:
          module_info_object.set("connection_fb_0")         #set Connection_FB 0

def refresh_fb():
    if client.power_status() == "ON":
        module_info_object.set("power_fb_1")
    else:
        module_info_object.set("power_fb_0")


if __name__ == "__main__":
    main()

if __name__ == "pyscript":
    main()

print("PYTHON: __name__ = " + __name__)

    
