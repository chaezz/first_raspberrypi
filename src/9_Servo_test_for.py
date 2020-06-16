import RPi.GPIO as GPIO #외부포트를 설정
import time
pin=25
GPIO.setmode(GPIO.BCM)# BCM타입을 사용한다고 지정
GPIO.setup(pin, GPIO.OUT)# OUTPUT MODE
p = GPIO.PWM(pin,50)
p.start(0)
try:
      while 1:
            angle = 2.5
            for i in range(0,10):
                  p.ChangeDutyCycle(angle)
                  angle += 1
                  print(angle)
                  time.sleep(0.5)
            
except KeyboardInterrupt :
      GPIO.cleanup()
      p.stop()
























            

            
