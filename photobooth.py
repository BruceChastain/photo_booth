import os
#import RPi.GPIO as GPIO
import time
import glob
import multiprocessing

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(10, GPIO.OUT)
#GPIO.setwarnings(False)
#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

os.system("killall gvfsd-gphoto2")
os.system("gphoto2 --auto-detect")
time.sleep(1)

def slide_multi_p():
    os.chdir("photos")
    os.system("feh -Y -x -q -D 4 -B black -F -Z -z -r")
    os.chdir("..")

if __name__ == '__main__':
    p = multiprocessing.Process(target=slide_multi_p)
    p.start()

def button_callback():
    p.join() #closes the multi thread and slide show
    os.chdir("count")
    os.system("feh -F --on-last-slide=quit -f countdown.lst --slideshow-delay .5")
    os.chdir("..")
    os.chdir("photos")
    os.system("gphoto2 --capture-image-and-download")
    new_pic  = max(glob.iglob('*[Jj][Pp][Gg]'), key=os.path.getctime)
    os.system("feh -F --on-last-slide=quit --slideshow-delay 7 --start-at " + (new_pic))
    os.chdir("..")
    p.start() #starts the multi threaded slide show

while True:
#    if GPIO.input(10) == GPIO.HIGH:
#        button_callback()
    print("running")
    time.sleep(.1)

