from django.http import FileResponse
from django.shortcuts import render, HttpResponse
from send2live.send2live import send_picture, send_ply_picture


#from api.send2api import send_picture, send_ply_picture

from compute.settings import DATA_PATH  #, API_SERVER, TEMP_PATH

def home(request):
    return render (request, 'home.html')

def test(request):
    return HttpResponse("Hello, Django!")

def sendply(request):
    path = DATA_PATH / "temp/faar.jpg"
    result = send_ply_picture("123", path)
    return HttpResponse("send_ply_picture: " + str(result))

def sendpicture(request):
    path = DATA_PATH / "temp/faar.jpg"
    result = send_picture("123", path)
    return HttpResponse("send_picture: " + str(result))

def errorlog(request):
    return FileResponse(open('/var/log/apache2/danbots/compute.err.log','rb'))
