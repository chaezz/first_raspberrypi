import RPi.GPIO as GPIO #외부포트를 설정
import time
pin=25
GPIO.setmode(GPIO.BCM)# BCM타입을 사용한다고 지정
GPIO.setup(pin, GPIO.OUT)# OUTPUT MODE
p = GPIO.PWM(pin,50)
p.start(0)
try:
      while 1:
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10.0)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5.0)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            
except KeyboardInterrupt :
      GPIO.cleanup()
      p.stop()
























            

            
