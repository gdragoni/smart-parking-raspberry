#!/usr/bin/python
#import picamera #trabalhar com a camera
import time #trabalhar com sleep
#from PIL import Image #trabalhar com imagens, carregar e criar imagens
#import pytesseract #realizar leituras a partir de imagens
#import requests #para realizar requisicoes
#import json #para trabalhar com JSON
import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'serviceAccountToken.json'

client = vision.ImageAnnotatorClient()

#URL = "http://smartparkingfho.herokuapp.com/vagas"
#requests_session = requests.session()
#requests_session.headers.update({'Content-Type': 'application/json'})
#requests_session.headers.update({'charset':'utf-8'})

#condicao = True
#while(condicao):

    #camera = picamera.PiCamera()

    #camera.resolution = (800, 600)

    #camera.start_preview()

    #time.sleep(2)

    #camera.capture('parking.jpg', resize=(640,480))

    #camera.stop_preview()

    #img =Image.open ('parking123.jpg')
    #text = pytesseract.image_to_string(img, lang='eng',config='--psm 6')


    #text2 = pytesseract.image_to_string(Image.open('parking123.jpg'),config='--oem 1 --psm 11' )

    #camera.close()

   # post_data = '[{"pos": "@1"},{"pos": "@2"},{"pos": "@3"},{"pos": "@4"},{"pos": "@5"},{"pos": "@6"},{"pos": "@7"}]'
    #post_data = '[{"pos": "@1"},{"pos": "@2"},{"pos": "@7"}]'
    #post_data = '[]'

  #  requests_response = requests_session.post(url=URL, data=post_data)

 #   print(requests_response)
    #print(text2)

#    break

    #time.sleep(5)

