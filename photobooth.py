import os
import RPi.GPIO as GPIO
import time
import glob

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

os.system("killall gvfsd-gphoto2")
os.system("gphoto2 --auto-detect")
time.sleep(2)

def button_callback():
    os.chdir("count")
    os.system("feh -F --on-last-slide=quit -f countdown.lst --slideshow-delay .5")
    os.chdir("..")
    os.chdir("photos")
    os.system("gphoto2 --capture-image-and-download")
    new_pic  = max(glob.iglob('*[Jj][Pp][Gg]'), key=os.path.getctime)
    os.system("feh -F --on-last-slide=quit --slideshow-delay 7 --start-at " + (new_pic))
    os.chdir("..")

while True:
    if GPIO.input(10) == GPIO.HIGH:
        button_callback()
    #print("running")
    #time.sleep(.1)

