
import os
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

os.system("killall gvfsd-gphoto2")

#os.system("gphoto2 --auto-detect")

def button_callback(channel):
    #Display countdown
    os.chdir("count")
    os.system("feh -F --cycle-once -f countdown.lst --slideshow-delay .1")
    #Take photo
    os.chdir("..")
    os.chdir("photos")
    os.system("gphoto2 --capture-image-and-download")
    #Display photo for X seconds
    #os.system("feh -F ")
    
def photo_rotate():
  
    #Play rotation of photos
    os.system("feh -Y -x -q -D 1 -B black -F -Z -z")
    

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)
    #button_callback()
    #photo_rotate()
message = input("press enter to quit")
GPIO.cleanup()
    