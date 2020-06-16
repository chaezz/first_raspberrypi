import RPi.GPIO as GPIO #외부포트를 설정
import time # 시간함수(지연시간을 설정할 때 사용하는 함수)

GPIO .setmode(GPIO.BCM)# BCM타입을 사용한다고 지정
GPIO .setup(16, GPIO.OUT)# OUTPUT MODE
GPIO .setup(25, GPIO.IN)# OUTPUT MODE



try:      
      while True:
            if GPIO.input(25)==True:
                GPIO.output(16, True)
                print("Switch On!!")
            else:
                GPIO.output(16, False)               
                
except KeyboardInterrupt:      
      GPIO.cleanup()#GPIO port close      



            
