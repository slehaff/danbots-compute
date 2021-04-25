#
# this module start the processing of the picture triplets
#
import os
import threading
from compute.settings import DATA_PATH #, TEMP_PATH
from .send2api import send_picture, send_ply_picture

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

#@background
def receive_pic_set(device, pic1, pic2, pic3):
    print("Picture received from device:", device)
    print(pic1, pic2, pic3)
    tmp_folder = DATA_PATH / 'temp'
    os.makedirs(tmp_folder, exist_ok=True)
    save_uploaded_file(pic1, tmp_folder / pic1.name )
    result = send_picture(device, tmp_folder / pic1.name )
    if not result:
        print("Send picture failed")
    result = send_ply_picture(device, tmp_folder / pic1.name )
    if not result:
        print("Send picture failed")

    return True

# def send_live_picture(deviceid, file_path):
#     print("deviceid", deviceid)
#     print("file path", file_path)

#     url = API_SERVER + PIC2D_FUNC

#     param = {'deviceid': deviceid, 'picture': "3D"}
#     try:
#         req = requests.post(url, timeout=HTTP_TIMEOUT, files={'picture': str(file_path)}, data=param)
#     except requests.exceptions.RequestException as ex:
#         print(ex)
#         return False
#     if req.status_code == requests.codes.ok:  #pylint: disable=no-member
#         print('det gik godt')
#         print(req.text)
#         return True
#     else:
#         print('Noget gik galt: ', req.status_code)
#         print(req.text)
#     return False
