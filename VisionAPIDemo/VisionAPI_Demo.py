import picamera #trabalhar com a camera
import time #trabalhar com sleep
import requests #para realizar requisicoes
import json #para trabalhar com JSON
import os, io
from google.cloud import vision
from google.cloud.vision import types

URL = "http://smartparkingfho.herokuapp.com/vagas"
requests_session = requests.session()
requests_session.headers.update({'Content-Type': 'application/json'})
requests_session.headers.update({'charset':'utf-8'})

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'serviceAccountToken.json'

client = vision.ImageAnnotatorClient()

FILE_NAME = 'parking.jpg'
#FILE_NAME = 'parking2.jpg'
FOLDER_PATH = r'/home/pi/Documents/SmartParking_new'


while(True):

    camera = picamera.PiCamera()

    camera.resolution = (800, 600)

    camera.start_preview()

    time.sleep(3)

    camera.capture(os.path.join(FOLDER_PATH, FILE_NAME))

    camera.stop_preview()

    camera.close()

    with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)

    vagas = response.text_annotations[0].description.replace("/","").replace("\n","").replace("I","")

    vagasList = vagas.split("@")

    post_data = "["
    for x in vagasList:
        if x :
            if vagasList.index(x) == len(vagasList)-1:
                post_data += """{"pos": """ + "\"@" + x + "\"" +"""}"""
            else:
                post_data += """{"pos": """ + "\"@" + x + "\"" +"""},"""
           
    post_data += "]"

    requests_response = requests_session.post(url=URL, data=post_data)

    print(requests_response)
    
    time.sleep(5)
