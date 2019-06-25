
import os
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
os.system("killall gvfsd-gphoto2")
os.system("gphoto2 --auto-detect")

def button_callback():
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

button_callback()
'''       
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
'''