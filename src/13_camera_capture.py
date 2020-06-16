from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

for i in range(5):
      sleep(1)
      camera.capture('/home/pi/Desktop/image%2.jpg'  % i)
camera.stop_preview()
