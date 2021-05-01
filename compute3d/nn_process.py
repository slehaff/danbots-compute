from time import sleep
from pathlib import Path
import threading
from PIL import Image, ImageOps
from compute3d.UNTruepredictV3 import nnprocess_input

COLOR_PICTURE = 'image8.jpg'
DIAS_PICTURE = 'image0.jpg'
NOLIGHT_PICTURE = 'image9.jpg'

def background(myfunction):
    '''
    a threading decorator
    use @background above the function you want to run in the background
    '''
    def bg_f(*a, **kw):
        print(myfunction.__name__)
        threading.Thread(target=myfunction, name=myfunction.__name__, args=a, kwargs=kw).start()
    return bg_f

def convert_picture(filepath, outfilepath):
    """ Convert from jpg to png """
    im1 = Image.open(filepath)
    im1.save(outfilepath)

def convert_blackwhite(filepath, outfilepath):
    """ convert from any(jpg,png) to greyscale (jpg,png) """
    im1 = Image.open(filepath)
    grey = ImageOps.grayscale(im1)
    grey.save(outfilepath)

#@background
def process_input(folder):
    """ Process a incoming folder with a pictureset """
    print("Processeing", folder)

    convert_picture(folder / COLOR_PICTURE, folder /'image8.png')
    convert_picture(folder / DIAS_PICTURE, folder /'image0.png')
    convert_picture(folder / NOLIGHT_PICTURE, folder /'image9.png')
    convert_blackwhite(folder / COLOR_PICTURE, folder / 'grey.png')

    #nnprocess_input(folder)
    

    print ("processing finish")
