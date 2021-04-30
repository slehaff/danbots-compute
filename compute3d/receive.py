#
# this module start the processing of the picture received from devices
#
import os
import threading
import datetime 
from compute.settings import DATA_PATH #, TEMP_PATH
from send2live.send2live import send_picture, send_ply_picture

def background(myfunction):
    '''
    a threading decorator
    use @background above the function you want to run in the background
    '''
    def bg_f(*a, **kw):
        print(myfunction.__name__)
        threading.Thread(target=myfunction, name=myfunction.__name__, args=a, kwargs=kw).start()
    return bg_f

def save_uploaded_file(handle, filepath):
    with open(filepath, 'wb+') as destination:
        for chunk in handle.chunks():
            destination.write(chunk)

def start_scan(device):
    print('Scan Start device:', device)
    return

#@background
def receive_pic_set(device, set_number, color_picture, french_picture, noligt_picture):
    print("Picture received device:", device, set_number)
     

    datestr = datetime.date.today().isoformat()
    tmp_folder = DATA_PATH / 'temp' / datestr

    os.makedirs(tmp_folder, exist_ok=True)
    save_uploaded_file(color_picture, tmp_folder / color_picture.name )
    save_uploaded_file(french_picture, tmp_folder / french_picture.name )
    save_uploaded_file(noligt_picture, tmp_folder / noligt_picture.name )
    result = send_picture(device, tmp_folder / color_picture.name )
    if not result:
        print("Send picture failed")
    #result = send_ply_picture(device, tmp_folder / pic1.name )
    #if not result:
    #    print("Send picture failed")

    return True

def stop_scan(device):
    print('Scan Stop device:', device)
    return
