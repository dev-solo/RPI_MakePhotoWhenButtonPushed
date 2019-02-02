
import time
import RPi.GPIO as GPIO
import picamera

BTN_PIN = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23

camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
try:
    btnLastSignal = GPIO.input(BTN_PIN) #start state of button
    hasPhoto = False #if we have photo
    while True:
         btnSignal = GPIO.input(BTN_PIN)
         if btnSignal == True and btnLastSignal == False :
             btnLastSignal = True
             hasPhoto = False
         elif btnSignal == False and btnLastSignal == True :
             if hasPhoto == False :
                timestamp = int(time.time())
                print("%d: Camera Make Shot" % timestamp)
                camera.capture("/home/pi/camera/photos/%d.jpg" % timestamp)
                time.sleep(0.3)
                hasPhoto = True
             btnLastSignal = False
except:
    GPIO.cleanup()
